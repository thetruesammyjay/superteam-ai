#!/bin/bash

# Start Telegram bot
echo "Starting Telegram bot..."
python src/bot/telegram_bot.py &

# Start Admin UI
echo "Starting Admin UI..."
python src/admin_ui/app.py &

# Start Twitter bot (if needed)
# echo "Starting Twitter bot..."
# python src/bot/twitter_bot.py &

echo "All services started!"