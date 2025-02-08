import unittest
from unittest.mock import patch
from src.llm.rag import RAG
from sentence_transformers import SentenceTransformer

class TestRAG(unittest.TestCase):
    def setUp(self):
        self.rag = RAG()

    @patch("sentence_transformers.SentenceTransformer.encode")
    def test_add_document(self, mock_encode):
        mock_encode.return_value = [0.1, 0.2, 0.3]
        self.rag.add_document("Test document")
        self.assertEqual(len(self.rag.documents), 1)

    @patch("sentence_transformers.SentenceTransformer.encode")
    def test_query(self, mock_encode):
        mock_encode.return_value = [0.1, 0.2, 0.3]
        self.rag.add_document("Test document")
        response = self.rag.query("Test query")
        self.assertEqual(response, "Test document")