import json
from config import Config

class JSONUtils:
    @staticmethod
    def load_json(file_path: str) -> dict:
        """Load JSON data from a file."""
        with open(file_path, "r") as f:
            return json.load(f)
    
    @staticmethod
    def save_json(data: dict, file_path: str):
        """Save JSON data to a file."""
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def add_member(member_data: dict, file_path: str = CONFIG.MEMBER_DATABASE):
        """Add a new member to the JSON Databse."""
        data = JSONUtils.load_json(file_path)
        member_id = str(len(data) + 1)
        data[member_id] = member_data
        JSONUtils.save_json(data, file_path)