import unittest
from unittest.mock import patch
from src.llm.semantic_search import SemanticSearch

class TestMemberFinder(unittest.TestCase):
    def setUp(self):
        self.semantic_search = SemanticSearch()

    @patch("src.llm.semantic_search.SentenceTransformer.encode")
    def test_search(self, mock_encode):
        mock_encode.return_value = [0.1, 0.2, 0.3]
        results = self.semantic_search.search("Find a Rust developer")
        self.assertIsInstance(results, list)