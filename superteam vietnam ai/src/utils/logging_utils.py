import logging
import os
from config import Config

def setup_logging(log_file: str = "system.log"):
    """Configure logging for the application."""
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s -%(name)s - %(levelname)s - %(message)s",
        handlers = [
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )