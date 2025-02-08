# Superteam Vietnam AI System

This project is an AI-driven solution designed to assist Superteam Vietnam in managing communication channels, content creation, and community inquiries. The system includes a **Telegram Knowledge Portal Bot**, **Superteam Member Finder**, **Twitter Management Assistant**, and **Content Advisor**, all powered by local LLMs for data privacy.

---

## Table of Contents

1. [Features](#features)
2. [Architecture](#architecture)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
   - [Telegram Knowledge Portal Bot](#telegram-knowledge-portal-bot)
   - [Superteam Member Finder](#superteam-member-finder)
   - [Twitter Management Assistant](#twitter-management-assistant)
   - [Content Advisor](#content-advisor)
5. [API Documentation](#api-documentation)
6. [Testing](#testing)
7. [Configuration](#configuration)
8. [File Structure](#file-structure)
9. [Docker Deployment](#docker-deployment)
10. [Contributing](#contributing)
11. [License](#license)

---

## Features

1. **Telegram Knowledge Portal Bot**:
   - Acts as a knowledge base for Superteam Vietnam.
   - Admins can upload documents to train the bot.
   - Uses **RAG (Retrieval-Augmented Generation)** for accurate responses.

2. **Superteam Member Finder**:
   - Matches community needs with relevant members using a JSON database.
   - Performs semantic search to suggest members or say "NO" if no match is found.

3. **Twitter Management Assistant**:
   - Proposes tweets for human approval.
   - Helps refine tweet drafts with keyword and handle suggestions.
   - Publishes approved tweets to the Superteam Twitter account.

4. **Content Advisor**:
   - Assists in creating and iterating content for Telegram and Twitter.
   - Enables collaborative conversations with human admins.

5. **Local LLM Deployment**:
   - Ensures data privacy by running all AI models locally.

---

## Architecture

The system is built using the following technologies:

- **Backend**: Python (FastAPI, Flask)
- **LLM**: Local LLMs (e.g., LLaMA 2, GPT-J, Falcon)
- **Vector Database**: FAISS for RAG
- **Frontend**: Admin UI built with FastAPI and Jinja2 templates
- **APIs**: Telegram Bot API, Twitter API
- **Data Storage**: JSON for member database, local files for documents
- **Containerization**: Docker for deployment

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/thetruesammyjay/superteam-ai.git
cd superteam-ai
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```


---

### **3. Set Up Environment Variables**


Create a `.env` file in the root directory and add the following variables:

```plaintext
# Telegram API
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# Twitter API
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret

# Local LLM
LOCAL_LLM_PATH=models/llama2/
EMBEDDINGS_PATH=models/embeddings/

# Data paths
DOCUMENTS_DIR=data/documents/
MEMBER_DATABASE=data/member_database.json
VECTOR_DB_PATH=data/vector_db/

# Logging
LOG_FILE=logs/system.log
```


---

### **4. Set Up Data and Models**



1. **Create the `data/` and `models/` folders**:
   ```bash
   mkdir -p data/documents data/vector_db logs models/llama2 models/embeddings
   ```
2. **Add the following files**:

- data/member_database.json: JSON database of Superteam members.

- models/llama2/: Local LLM model files (e.g., LLaMA 2).

- models/embeddings/: Pre-trained embeddings for semantic search.


---

### **5. Run the System**



1. Start the Telegram bot:
   ```bash
   python src/bot/telegram_bot.py
   ```


---

### **6. Usage**



### Telegram Knowledge Portal Bot
- Interact with the bot on Telegram.
- Admins can upload documents via the Admin UI to train the bot.
- The bot uses RAG to answer user queries or respond with "NO" if no relevant information is found.

### Superteam Member Finder
- Use the `/member/find` API endpoint to search for members:
  ```bash
  curl -X POST "http://127.0.0.1:8000/member/find" -H "Content-Type: application/json" -d '{"query": "Find a Rust developer"}'


---

### **7. API Documentation**



### 1. Telegram Bot API
- **Endpoint**: `/telegram/send_message`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "text": "What is Superteam Vietnam?"
  }

### 2. Twitter API
- **Endpoint**: '/twitter/propose_tweet'
- **Method**: POST
- **Request Body** :
  ```json
  {
  "text": "Join Superteam Vietnam!"
  }

### 3. Member Finder API
- **Endpoint**: '/member/find'
- **Method**: POST
- **Request Body**: 
  ```json
  {
  "query": "Find a Rust developer"
  }
  ```

---

### **8. Testing**

Run all tests using pytest:
```bash
pytest tests/
```

---

### **9. Configuration**



The `config.py` file centralizes all configuration settings. Key configurations include:
- Telegram and Twitter API keys.
- Paths for local LLM models and embeddings.
- Data directories for documents, member database, and vector database.


### **10. File Structure**

```markdown
superteam-ai/
├── src/
│   ├── api/                    # API endpoints
│   ├── bot/                    # Core bot logic
│   ├── llm/                    # Local LLM integration
│   ├── utils/                  # Utility functions
│   ├── admin_ui/               # Admin UI for document upload
│   └── config.py               # Configuration settings
├── tests/                      # Unit and integration tests
├── data/                       # Data storage
│   ├── documents/              # Uploaded documents
│   ├── member_database.json    # JSON database of Superteam members
│   └── vector_db/              # Vector database for RAG
├── logs/                       # Log files
│   └── system.log              # System logs
├── models/                     # Local LLM models
│   ├── llama2/                 # LLaMA 2 model files
│   └── embeddings/             # Pre-trained embeddings
├── scripts/                    # Utility scripts
├── Dockerfile                  # Docker image definition
├── docker-compose.yml          # Docker Compose configuration
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # Project documentation
```

---
## **10. Docker Deployment**

### 1. Build the Docker Image
```bash
docker-compose build
```

### 2. Start the Services
```bash
docker-compose up
```

### 3. Access the Admin UI
- Open your browser and navigate to http://localhost:8000/.

### 4. Stop the services
```bash
docker-compose down
```


---

### **11. Contributing**



Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---
### **12. License**

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
