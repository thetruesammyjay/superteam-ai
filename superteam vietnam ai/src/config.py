import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Telegram API
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # Twitter API
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

    # Local LLM
    LOCAL_LLM_PATH = os.getenv("LOCAL_LLM_PATH", "models/llama2/")
    EMBEDDINGS_PATH = os.getenv("EMBEDDINGS_PATH", "models/embeddings/")

    # Data paths
    DOCUMENTS_DIR = os.getenv("DOCUMENTS_DIR", "data/documents/")
    MEMBER_DATABASE = os.getenv("MEMBER_DATABASE", "data/member_database.json")
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "data/vector_db/")

    # Logging
    LOG_FILE = os.getenv("LOG_FILE", "logs/system.log")