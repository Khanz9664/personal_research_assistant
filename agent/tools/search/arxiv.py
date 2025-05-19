"""
ArXiv API integration for academic paper search.
"""
import arxiv
from typing import List, Dict, Any
from ..base import BaseTool

class ArxivSearch(BaseTool):
    def __init__(self):
        self.client = arxiv.Client()
        
    async def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Search ArXiv for relevant papers."""
        try:
            search = arxiv.Search(
                query=query,
                max_results=10,
                sort_by=arxiv.SortCriterion.Relevance
            )
            
            results = []
            async for paper in self.client.results(search):
                results.append({
                    "title": paper.title,
                    "authors": [author.name for author in paper.authors],
                    "summary": paper.summary,
                    "pdf_url": paper.pdf_url,
                    "published": paper.published.isoformat(),
                    "categories": paper.categories,
                    "doi": paper.doi
                })
                
            return {
                "success": True,
                "sources": results,
                "tool": "arxiv"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "tool": "arxiv"
            }