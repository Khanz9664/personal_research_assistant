"""
Tool registry for managing and accessing research tools.
"""
from typing import Dict, Type
from .base import BaseTool
from .search import (
    ArxivSearch,
    GoogleScholarSearch,
    SerpAPISearch,
    PapersWithCodeSearch,
    HuggingFaceSearch,
    GitHubSearch
)
from .content import (
    PDFExtractor,
    WebScraper,
    CodeExtractor
)
from .analysis import (
    TextSummarizer,
    CodeAnalyzer,
    DataAnalyzer
)
from .generation import ReportGenerator

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, BaseTool] = {
            # Search tools
            "arxiv": ArxivSearch(),
            "google_scholar": GoogleScholarSearch(),
            "web_search": SerpAPISearch(),
            "papers_with_code": PapersWithCodeSearch(),
            "huggingface": HuggingFaceSearch(),
            "github": GitHubSearch(),
            
            # Content extraction
            "pdf": PDFExtractor(),
            "web": WebScraper(),
            "code": CodeExtractor(),
            
            # Analysis tools
            "summarizer": TextSummarizer(),
            "code_analyzer": CodeAnalyzer(),
            "data_analyzer": DataAnalyzer(),
            
            # Generation tools
            "report": ReportGenerator()
        }
        
    def get_tool_for_task(self, task: str) -> BaseTool:
        """Select most appropriate tool based on task description."""
        task_lower = task.lower()
        
        if "implementation" in task_lower or "code" in task_lower:
            return self.tools["papers_with_code"]
        elif "model" in task_lower or "dataset" in task_lower:
            return self.tools["huggingface"]
        elif "github" in task_lower or "repository" in task_lower:
            return self.tools["github"]
        elif "arxiv" in task_lower or "paper" in task_lower:
            return self.tools["arxiv"]
        elif "data" in task_lower:
            return self.tools["data_analyzer"]
        else:
            return self.tools["web_search"]
            
    def get_tool(self, name: str) -> BaseTool:
        return self.tools.get(name)