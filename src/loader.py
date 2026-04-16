import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from src.database.db import Database


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
db = Database()

commands = [
    types.BotCommand(command="help", description="List of commands"),
    types.BotCommand(command="week", description="Get the week schedule"),
    types.BotCommand(command="today", description="Get the today schedule"),
    types.BotCommand(command="tomorrow", description="Get the tomorrow schedule"),
    types.BotCommand(command="yesterday", description="Get the yesterday schedule"),
    types.BotCommand(command="specific_day", description="Get the specific day schedule"),
]