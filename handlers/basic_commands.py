from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command

from utils.formatters.basic_commands import *
from utils.keyboards.main_kb import *


router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message):
    text = start_command(message.from_user.full_name)
    keyboard = get_main_kb()
    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=keyboard)


@router.message(Command("help"))
async def command_help(message: types.Message):
    text = help_command()
    await message.answer(text, parse_mode=ParseMode.HTML)
