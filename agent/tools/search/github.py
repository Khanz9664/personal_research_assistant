"""
GitHub API integration for code search and repository analysis.
"""
from typing import Dict, Any
from github import Github
from ..base import BaseTool

class GitHubSearch(BaseTool):
    def __init__(self, token: str = None):
        self.github = Github(token)
        
    async def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Search GitHub for relevant repositories and code."""
        try:
            # Search repositories
            repos = self.github.search_repositories(
                query=query,
                sort="stars",
                order="desc"
            )
            
            results = []
            for repo in repos[:5]:  # Get top 5 results
                # Get README content
                try:
                    readme = repo.get_readme().decoded_content.decode('utf-8')
                except:
                    readme = ""
                
                # Get requirements/dependencies
                dependencies = []
                try:
                    if repo.get_contents("requirements.txt"):
                        deps = repo.get_contents("requirements.txt").decoded_content.decode('utf-8')
                        dependencies = [d.strip() for d in deps.split('\n') if d.strip()]
                except:
                    pass
                
                results.append({
                    'name': repo.name,
                    'full_name': repo.full_name,
                    'description': repo.description,
                    'url': repo.html_url,
                    'stars': repo.stargazers_count,
                    'forks': repo.forks_count,
                    'language': repo.language,
                    'topics': repo.get_topics(),
                    'readme': readme,
                    'dependencies': dependencies,
                    'last_updated': repo.updated_at.isoformat()
                })
            
            return {
                'success': True,
                'sources': results,
                'tool': 'github'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'tool': 'github'
            }