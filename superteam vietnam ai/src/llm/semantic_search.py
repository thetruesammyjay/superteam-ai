from sentence_transformers import SentenceTransformer
import numpy as np
import json
from config import Config

class SemanticSearch:
    def __init__(self):
        self.embeddings_model = SentenceTransformer(Config.EMBEDDINGS_PATH)
        with open(Config.MEMBER_DATABASE, "r") as f:
            self.member_data = json.load(f)
        self.member_embeddings = self._precompute_embeddings()

    def _precompute_embeddings(self):
        embeddings = {}
        for member_id, member_info in self.member_data.items():
            text = f"{member_info['name']} {member_info['skills']} {member_info['projects']}"
            embeddings[member_id] = self.embeddings_model.encode(text)
        return embeddings
    
    def search(self, query: str, top_5: int = 3):
        query_embedding = self.embeddings_model.encode(query)
        results = []
        for member_id, embedding in self.member_embeddings.items():
            similarity = np.dot(query_embedding, embedding)
            results.append((member_id, similarity))
        results.sort(key=lambda x: x[1], reverse=True)
        return [self.member_data[member_id] for member_id, _ in results[:top_k]]