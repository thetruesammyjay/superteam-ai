from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bot.twitter_bot import TwitterBot
from config import Config

app = FastAPI()
twitter_bot = TwitterBot()

class TweetDraft(BaseModel):
    text: str

@app.post("/twitter/propose_tweet")
async def propose_tweet(draft: TweetDraft):
    try:
        # Generate a tweet draft
        proposed_tweet = twitter_bot.propose_tweet(draft.text)
        return {"status": "success", "proposed_tweet": proposed_tweet}
    except Exceptiona as e:
        raise HTTPExecution(status_code=500, detail=str(e))

@app.post("twitter/publish_tweet")
async def publish_tweet(draft: TweetDraft):
    try:
        # Publish the tweet
        tweet_id = twitter_bot.publish_tweet(draft.text)
        return {"status": "success", "tweet_id": tweet_id}
    except Exception as e:
        raise HTTPExecution(status_code=500, detail=str(e))