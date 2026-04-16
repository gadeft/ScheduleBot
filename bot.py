import asyncio
import logging

from aiogram_dialog import setup_dialogs

from src.handlers import chooseday, calendar, schedule, register
from src.loader import bot, dp, db, commands


logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_router(register.router)

    # dp.include_router(basic_commands.router)
    dp.include_router(calendar.router)
    dp.include_router(schedule.router)
    dp.include_router(chooseday.router)

    setup_dialogs(dp)

    dp.include_router(calendar.dialog)

    await bot.set_my_commands(commands)

    await db.connect()
    await db.create_students_table()
    await db.create_lecturers_table()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    await db.close()


if __name__ == '__main__':
    asyncio.run(main())