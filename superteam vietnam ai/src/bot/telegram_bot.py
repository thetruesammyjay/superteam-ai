from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from llm.rag import RAG
from config import Config

class TelegramBot:
    def __init__(self):
        self.rag = RAG()
    
    async def start(self, update: Update, context):
        await update.message.reply_text("Hello! I'm the Superteam Vietnam. Ask me anything! ")

    async def handle_message(self, update: Update, context):
        question = update.message.text
        response = self.rag.query(question)
        await update.message.reply_text(response)
    
    def run(self):
        app = ApplicationBuilder().token(Config.TELEGRAM_BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(MessageHandler(filters.TEXT, self.handle_message))
        app.run_polling()