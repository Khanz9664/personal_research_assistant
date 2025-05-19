"""
Long-term memory implementation with vector embeddings for semantic search.
"""
from typing import List, Dict, Any
import json
import numpy as np
from datetime import datetime
from sentence_transformers import SentenceTransformer
import faiss

class LongTermMemory:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = 384  # Output dimension of the model
        self.index = faiss.IndexFlatL2(self.dimension)
        self.sessions = []
        self.embeddings = []
        
    def store_session(self, session: Dict[str, Any]):
        """Store research session with vector embeddings."""
        # Create text representation of session
        session_text = f"{session['query']} {session['domain']} " + \
                      " ".join([info['content'] for info in session['extracted_info']]) + \
                      " ".join([step['reasoning'] for step in session['reasoning_steps']]) + \
                      " ".join([c['text'] for c in session['conclusions']])
        
        # Generate embedding
        embedding = self.model.encode([session_text])[0]
        
        # Store session and embedding
        self.sessions.append(session)
        if len(self.embeddings) == 0:
            self.embeddings = embedding.reshape(1, -1)
        else:
            self.embeddings = np.vstack([self.embeddings, embedding.reshape(1, -1)])
        
        # Update FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)
        
    def semantic_search(self, query: str, k: int = 3) -> List[Dict[str, Any]]:
        """Search for relevant past sessions using semantic similarity."""
        # Generate query embedding
        query_embedding = self.model.encode([query])
        
        # Search index
        distances, indices = self.index.search(query_embedding, k)
        
        # Return relevant sessions
        results = []
        for idx in indices[0]:
            if idx < len(self.sessions):
                results.append(self.sessions[idx])
                
        return results
        
    def save(self, path: str):
        """Save memory state to disk."""
        state = {
            "sessions": self.sessions,
            "embeddings": self.embeddings.tolist() if len(self.embeddings) > 0 else []
        }
        with open(path, 'w') as f:
            json.dump(state, f)
            
    def load(self, path: str):
        """Load memory state from disk."""
        with open(path, 'r') as f:
            state = json.load(f)
            self.sessions = state["sessions"]
            self.embeddings = np.array(state["embeddings"])
            if len(self.embeddings) > 0:
                self.index = faiss.IndexFlatL2(self.dimension)
                self.index.add(self.embeddings)