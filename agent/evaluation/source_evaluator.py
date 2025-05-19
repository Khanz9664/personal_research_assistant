"""
Source evaluation and filtering based on quality heuristics.
"""
from typing import List, Dict, Any
import re

class SourceEvaluator:
    def __init__(self):
        self.domain_criteria = {
            "ml": {
                "domains": [
                    "arxiv.org",
                    "papers.nips.cc",
                    "openreview.net",
                    "github.com",
                    "huggingface.co",
                    "pytorch.org",
                    "tensorflow.org"
                ],
                "keywords": [
                    "deep learning",
                    "neural network",
                    "transformer",
                    "machine learning",
                    "dataset",
                    "benchmark",
                    "implementation"
                ]
            },
            "data_science": {
                "domains": [
                    "kaggle.com",
                    "scipy.org",
                    "pandas.pydata.org",
                    "scikit-learn.org"
                ],
                "keywords": [
                    "data analysis",
                    "visualization",
                    "statistics",
                    "pandas",
                    "numpy",
                    "matplotlib"
                ]
            }
        }
        
    def filter_sources(
        self,
        sources: List[Dict[str, Any]],
        domain: str = "ml"
    ) -> List[Dict[str, Any]]:
        """Filter and rank sources based on quality criteria."""
        criteria = self.domain_criteria.get(domain, self.domain_criteria["ml"])
        
        scored_sources = []
        for source in sources:
            score = self._calculate_score(source, criteria)
            if score > 0:
                scored_sources.append({
                    **source,
                    "quality_score": score
                })
                
        # Sort by score and return top results
        return sorted(
            scored_sources,
            key=lambda x: x["quality_score"],
            reverse=True
        )[:5]
        
    def _calculate_score(
        self,
        source: Dict[str, Any],
        criteria: Dict[str, List[str]]
    ) -> float:
        """Calculate quality score for a source."""
        score = 0.0
        
        # Domain authority
        url = source.get("url", "").lower()
        for domain in criteria["domains"]:
            if domain in url:
                score += 2.0
                break
                
        # Keyword relevance
        text = (
            source.get("title", "") +
            source.get("description", "") +
            source.get("summary", "")
        ).lower()
        
        for keyword in criteria["keywords"]:
            if keyword in text:
                score += 1.0
                
        # Citations/stars if available
        if "citations" in source:
            score += min(source["citations"] / 100, 3.0)
            
        if "stars" in source:
            score += min(source["stars"] / 1000, 2.0)
            
        # Recency bonus
        if "published" in source:
            year = int(re.findall(r'\d{4}', source["published"])[0])
            if year >= 2023:
                score += 1.5
            elif year >= 2021:
                score += 1.0
                
        return score