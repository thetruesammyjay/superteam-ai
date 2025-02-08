from fastapi import FASTAPI, HTTPException
from pydantic import BaseModel
from bot.telegram_bot import TelegramBot
from config import Config

app = FastAPI()
telegram_bot = TelegramBot()

class TelegramMessage(BaseModel):
    text: str

@app.post("/telegram/send_message")
async def send_message(message: TelegramMessage):
    try:
        # This is a simulation so replace with actual logic
        response = telegram_bot.handle_message(message.text)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("startup")
async def startup_event():
    telegram_bot.run()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)