"""
Hugging Face Hub API integration for models and datasets.
"""
from typing import Dict, Any
from huggingface_hub import HfApi
from ..base import BaseTool

class HuggingFaceSearch(BaseTool):
    def __init__(self):
        self.api = HfApi()
        
    async def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Search for models and datasets on Hugging Face Hub."""
        try:
            # Search models
            models = self.api.list_models(
                search=query,
                limit=5,
                sort="downloads",
                direction=-1
            )
            
            # Search datasets
            datasets = self.api.list_datasets(
                search=query,
                limit=5,
                sort="downloads",
                direction=-1
            )
            
            results = []
            
            # Process models
            for model in models:
                results.append({
                    'type': 'model',
                    'name': model.modelId,
                    'downloads': model.downloads,
                    'likes': model.likes,
                    'tags': model.tags,
                    'url': f"https://huggingface.co/{model.modelId}"
                })
                
            # Process datasets
            for dataset in datasets:
                results.append({
                    'type': 'dataset',
                    'name': dataset.id,
                    'downloads': dataset.downloads,
                    'likes': dataset.likes,
                    'tags': dataset.tags,
                    'url': f"https://huggingface.co/datasets/{dataset.id}"
                })
            
            return {
                'success': True,
                'sources': results,
                'tool': 'huggingface'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'tool': 'huggingface'
            }