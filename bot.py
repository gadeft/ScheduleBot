import asyncio
import logging

from src.db.session import async_session

# from aiogram_dialog import setup_dialogs

from src.handlers import register
from src.loader import bot, dp, commands, init_db
from src.db.middleware import DbSessionMiddleware


logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_router(register.router)

    # # dp.include_router(basic_commands.router)
    # dp.include_router(calendar.router)
    # dp.include_router(schedule.router)
    # dp.include_router(chooseday.router)
    #
    # setup_dialogs(dp)
    #
    # dp.include_router(calendar.dialog)

    dp.update.middleware(DbSessionMiddleware(async_session))

    await bot.set_my_commands(commands)

    await bot.delete_webhook(drop_pending_updates=True)

    await init_db()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())