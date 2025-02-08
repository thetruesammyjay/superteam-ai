import unittest
from unittest.mock import patch
from src.bot.telegram_bot import TelegramBot
from src.llm.rag import RAG

class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.telegram_bot = TelegramBot()

    @patch("src.bot.telegram_bot.ApplicationBuilder")
    def test_run(self, mock_app_builder):
        self.telegram_bot.run()
        mock_app_builder.assert_called_once()

    @patch("src.llm.rag.RAG.query")
    def test_handle_message(self, mock_rag_query):
        mock_rag_query.return_value = "Test response"
        response = self.telegram_bot.handle_message("Test query")
        self.assertEqual(response, "Test response")