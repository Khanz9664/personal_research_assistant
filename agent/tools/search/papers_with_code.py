"""
Papers with Code API integration for ML benchmarks and implementations.
"""
from typing import Dict, Any
from paperswithcode import PapersWithCodeClient
from ..base import BaseTool

class PapersWithCodeSearch(BaseTool):
    def __init__(self):
        self.client = PapersWithCodeClient()
        
    async def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Search for papers with code implementations."""
        try:
            # Search papers
            papers = self.client.paper_list(query)
            
            results = []
            for paper in papers[:10]:  # Get top 10 results
                # Get implementations
                implementations = self.client.paper_implementations(paper.id)
                
                # Get evaluation results if available
                evaluations = []
                for impl in implementations:
                    if impl.results:
                        evaluations.extend([{
                            'metric': result.metric,
                            'value': result.value,
                            'dataset': result.dataset
                        } for result in impl.results])
                
                results.append({
                    'title': paper.title,
                    'abstract': paper.abstract,
                    'url': paper.url,
                    'github_url': paper.github,
                    'paper_url': paper.paper_url,
                    'implementations': [{
                        'url': impl.url,
                        'framework': impl.framework,
                        'stars': impl.stars
                    } for impl in implementations],
                    'evaluations': evaluations
                })
            
            return {
                'success': True,
                'sources': results,
                'tool': 'papers_with_code'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'tool': 'papers_with_code'
            }