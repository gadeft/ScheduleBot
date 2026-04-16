from aiogram import Router
from aiogram.filters.command import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from src.utils.keyboards.register import get_vertical_kb
from src.utils.callbacks.register import RoleCD
from src.utils.formatters.register import TEXT, TEXT_TEMPLATES

from src.constants.roles import ROLES, FUNCTIONS_ROLES


# TODO: if needed, move this function to a new python file utils/exceptions/register.py
def role_not_found(callback_data: CallbackData):
    raise TypeError(f"This role doesn't exist\nThe callback data {callback_data}")


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    kb = get_vertical_kb(
        callback_data=RoleCD,
        text_template=TEXT_TEMPLATES["role"],
        values=ROLES
    )

    await message.answer(text=TEXT["choose_role"], reply_markup=kb, parse_mode=ParseMode.HTML)


@router.callback_query(RoleCD.filter())
async def role_chosen(query: CallbackQuery, state: FSMContext, callback_data: RoleCD):
    await query.answer()

    await state.update_data(role=callback_data.value)

    await query.message.delete()

    entry_func_for_role = FUNCTIONS_ROLES.get(callback_data.value, lambda: role_not_found(callback_data))
    await entry_func_for_role(message=query.message, state=state)