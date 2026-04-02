import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram_dialog import setup_dialogs
from dotenv import load_dotenv

from handlers import basic_commands
from handlers import schedule
from handlers import calendar
from handlers import chooseday


logging.basicConfig(level=logging.INFO)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

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

async def main():
    dp.include_router(basic_commands.router)
    dp.include_router(calendar.router)
    dp.include_router(schedule.router)
    dp.include_router(chooseday.router)

    setup_dialogs(dp)

    dp.include_router(calendar.dialog)

    await bot.set_my_commands(commands)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())