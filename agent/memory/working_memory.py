"""
Working memory implementation for storing current research session data.
"""
from typing import Dict, List, Any
from datetime import datetime
import json

class WorkingMemory:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.session = {
            "start_time": datetime.now().isoformat(),
            "query": "",
            "domain": "",
            "sources": [],
            "extracted_info": [],
            "reasoning_steps": [],
            "conclusions": []
        }
        
    def start_session(self, query: str = "", domain: str = ""):
        self.reset()
        self.session["query"] = query
        self.session["domain"] = domain
        
    def store_result(self, result: Dict[str, Any]):
        """Store research result with metadata."""
        if result.get("sources"):
            self.session["sources"].extend(result["sources"])
            
        if result.get("content"):
            self.session["extracted_info"].append({
                "timestamp": datetime.now().isoformat(),
                "content": result["content"],
                "source": result.get("source", "unknown"),
                "tool": result.get("tool", "unknown")
            })
            
        if result.get("reasoning"):
            self.session["reasoning_steps"].append({
                "timestamp": datetime.now().isoformat(),
                "reasoning": result["reasoning"]
            })
            
    def add_conclusion(self, conclusion: str):
        self.session["conclusions"].append({
            "timestamp": datetime.now().isoformat(),
            "text": conclusion
        })
        
    def get_session(self) -> Dict[str, Any]:
        """Get current session data."""
        return self.session
        
    def save_session(self, path: str):
        """Save session to disk."""
        with open(path, 'w') as f:
            json.dump(self.session, f, indent=2)