from sentence_transformers import SentenceTransformer
from faiss import IndexFlatL2
import numpy as np
import os
from config import Config

class RAG:
    def __init__(self):
        self.embeddings_model = SentenceTransformer(Config.EMBEDDINGS_PATH)
        self.vector_db = IndexFlatL2(768)
        self.documents = []

    def add_document(self, text: str):
        embedding = self.embeddings_model.encode(text)
        self.vector_db.add(np.array([embedding]))
        self.documents.append(text)
    
    def query(self, question: str, top_k: int = 1):
        embedding = self.embeddings_model.encode(question)
        distances, indices = self.vector_db.search(np.array([embedding]), top_k)
        if distances[0][0] > 0.8:
            return "NO"
        return self.documents[indices[0][0]]