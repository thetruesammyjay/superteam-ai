# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ENV TWITTER_API_KEY=your_twitter_api_key
ENV TWITTER_API_SECRET=your_twitter_api_secret
ENV TWITTER_ACCESS_TOKEN=your_twitter_access_token
ENV TWITTER_ACCESS_SECRET=your_twitter_access_secret
ENV LOCAL_LLM_PATH=/app/models/llama2/
ENV EMBEDDINGS_PATH=/app/models/embeddings/
ENV DOCUMENTS_DIR=/app/data/documents/
ENV MEMBER_DATABASE=/app/data/member_database.json
ENV VECTOR_DB_PATH=/app/data/vector_db/
ENV LOG_FILE=/app/logs/system.log

# Create necessary directories
RUN mkdir -p /app/data/documents /app/data/vector_db /app/logs /app/models/llama2 /app/models/embeddings

# Expose ports
EXPOSE 8000

# Start the Admin UI and Telegram bot
CMD ["bash", "scripts/start_services.sh"]