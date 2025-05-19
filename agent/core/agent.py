"""
Core Agent class implementing the main autonomous loop and orchestration.
"""
from typing import List, Dict, Any
from dataclasses import dataclass
import logging

from .memory import WorkingMemory, LongTermMemory
from .planning import TaskPlanner
from .tools import ToolRegistry
from .evaluation import SourceEvaluator
from .prompts import SystemPrompts

@dataclass
class AgentState:
    current_task: str
    subtasks: List[str]
    completed_tasks: List[str]
    failed_tasks: List[str]
    context: Dict[str, Any]

class ResearchAgent:
    def __init__(self, config: Dict[str, Any]):
        self.working_memory = WorkingMemory()
        self.long_term_memory = LongTermMemory()
        self.planner = TaskPlanner()
        self.tools = ToolRegistry()
        self.evaluator = SourceEvaluator()
        self.system_prompts = SystemPrompts()
        self.state = AgentState(
            current_task="",
            subtasks=[],
            completed_tasks=[],
            failed_tasks=[],
            context={}
        )
        
    async def research(self, query: str, domain: str = "ml", depth: str = "deep") -> str:
        """Main research loop that coordinates the autonomous research process."""
        try:
            # Initialize research session
            self.state.current_task = query
            self.working_memory.start_session()
            
            # Generate initial research plan
            research_plan = await self.planner.create_research_plan(
                query, 
                domain,
                depth
            )
            self.state.subtasks = research_plan.tasks
            
            # Main research loop
            while self.should_continue():
                next_task = self.planner.get_next_task(self.state)
                
                if not next_task:
                    break
                    
                try:
                    # Execute task using appropriate tools
                    result = await self.execute_task(next_task)
                    
                    # Evaluate and store results
                    if result.success:
                        self.working_memory.store_result(result)
                        self.state.completed_tasks.append(next_task)
                    else:
                        self.state.failed_tasks.append(next_task)
                        
                    # Update research plan based on new findings
                    self.state.subtasks = await self.planner.refine_plan(
                        self.state,
                        self.working_memory
                    )
                    
                except Exception as e:
                    logging.error(f"Task execution failed: {str(e)}")
                    self.state.failed_tasks.append(next_task)
            
            # Generate final report
            report = await self.generate_report()
            
            # Store session in long-term memory
            self.long_term_memory.store_session(
                self.working_memory.get_session()
            )
            
            return report
            
        except Exception as e:
            logging.error(f"Research process failed: {str(e)}")
            return self.generate_error_report(str(e))
    
    async def execute_task(self, task: str) -> Dict[str, Any]:
        """Execute a single research task using appropriate tools."""
        tool = self.tools.get_tool_for_task(task)
        result = await tool.execute(task, self.state.context)
        
        if result.sources:
            result.sources = self.evaluator.filter_sources(
                result.sources,
                domain=self.state.context.get("domain", "ml")
            )
            
        return result
    
    def should_continue(self) -> bool:
        """Determine if research should continue based on current state."""
        return (
            len(self.state.subtasks) > 0 and
            len(self.state.completed_tasks) < 10 and
            len(self.state.failed_tasks) < 3
        )
    
    async def generate_report(self) -> str:
        """Generate final research report from working memory."""
        session_data = self.working_memory.get_session()
        return await self.tools.report_generator.generate(session_data)