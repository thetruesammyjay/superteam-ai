import tweepy
from llm.local_llm import LocalLLM
from config import Config

class TwitterBot:
    def __init__(self):
        self.llm = LocalLLM()
        self.client = tweepy.Client(
            consumer_key=Config.TWITTER_API_KEY,
            consumer_secret= Config.TWITTER_API_SECRET,
            access_token = Config.TWITTER_ACCESS_TOKEN,
            access_token_secret = Config.TWITTER_ACCESS_SECRET,
        )
    
    def propose_tweet(self, prompt: str):
        # Generate a tweet draft using the local LLM
        tweet_draft = self.llm.generate(f"Propose a tweet about: {prompt}", max_tokens=50)
        return tweet_draft
    
    def publish_tweet(self, text: str):
        # Publish the tweet to the Superteam Twitter account
        response = self.client.create_tweet(text=text)
        return response.data["id"]