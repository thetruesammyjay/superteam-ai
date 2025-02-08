import unittest
from unittest.mock import patch
from src.bot.twitter_bot import TwitterBot
from src.llm.local_llm import LocalLLM

class TestTwitterBot(unittest.TestCase):
    def setUp(self):
        self.twitter_bot = TwitterBot()

    @patch("src.llm.local_llm.LocalLLM.generate")
    def test_propose_tweet(self, mock_generate):
        mock_generate.return_value = "Test tweet"
        tweet_draft = self.twitter_bot.propose_tweet("Test prompt")
        self.assertEqual(tweet_draft, "Test tweet")

    @patch("tweepy.Client.create_tweet")
    def test_publish_tweet(self, mock_create_tweet):
        mock_create_tweet.return_value = {"data": {"id": "12345"}}
        tweet_id = self.twitter_bot.publish_tweet("Test tweet")
        self.assertEqual(tweet_id, "12345")