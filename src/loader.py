import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from src.db.engine import engine
from src.db.base import Base


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


bot = Bot(BOT_TOKEN)
dp = Dispatcher()

commands = [
    types.BotCommand(command="help", description="List of commands"),
    types.BotCommand(command="week", description="Get the week schedule"),
    types.BotCommand(command="today", description="Get the today schedule"),
    types.BotCommand(command="tomorrow", description="Get the tomorrow schedule"),
    types.BotCommand(command="yesterday", description="Get the yesterday schedule"),
    types.BotCommand(command="specific_day", description="Get the specific day schedule"),
]