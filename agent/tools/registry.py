"""
Tool registry for managing and accessing research tools.
"""
from typing import Dict, Type
from .base import BaseTool
from .search import (
    ArxivSearch,
    SemanticScholarSearch,
    GoogleScholarSearch,
    SerpAPISearch
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
            "semantic_scholar": SemanticScholarSearch(),
            "google_scholar": GoogleScholarSearch(),
            "web_search": SerpAPISearch(),
            
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
        if "arxiv" in task.lower():
            return self.tools["arxiv"]
        elif "code" in task.lower():
            return self.tools["code"]
        elif "data" in task.lower():
            return self.tools["data_analyzer"]
        else:
            return self.tools["web_search"]
            
    def get_tool(self, name: str) -> BaseTool:
        return self.tools.get(name)