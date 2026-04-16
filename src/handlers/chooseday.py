from aiogram.fsm.state import StatesGroup, State

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_dialog import DialogManager

from src.handlers import calendar


class ChooseDay(StatesGroup):
    waiting_for_day = State()


router = Router()


@router.message(Command("schedule"))
async def cmd_choose_day(message: Message, state: FSMContext):
    await message.answer("Enter group ID:")

    await state.set_state(ChooseDay.waiting_for_day)


@router.message(ChooseDay.waiting_for_day)
async def process_day(message: Message, dialog_manager: DialogManager, state: FSMContext):
    group_id = message.text

    await calendar.cmd_specific_day(message, dialog_manager, group_id)

    await state.clear()