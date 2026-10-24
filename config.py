from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()
bottoken = os.getenv("BOT_TOKEN")
if not bottoken:
    raise ValueError("Bot Token not found\n"
                     "Put it in your .env file.\n")
bot = Bot(token=bottoken)
dp = Dispatcher()
