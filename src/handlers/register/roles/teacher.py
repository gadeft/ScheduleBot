from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.keyboards.register import get_vertical_kb
from src.utils.callbacks.register import TeacherCD
from src.utils.states.register import RegisterSG
from src.utils.formatters.register import (
    TEXT, TEXT_TEMPLATES, TEACHERS, teacher_finish_text
)
from src.db.repo import make_user_lecturer


router = Router()


async def search_teacher(message: Message, state: FSMContext):
    await state.set_state(RegisterSG.search_teacher)
    await message.answer(text=TEXT["search_teacher"], parse_mode=ParseMode.HTML)


@router.message(RegisterSG.search_teacher)
async def choose_teacher(message: Message, state: FSMContext):
    user_input = message.text.lower()
    found = list()

    for i in TEACHERS:
        if user_input in i.lower():
            found.append(i)

    if not found:
        await message.answer(text=TEXT["not_found_teacher"])
        return

    kb = get_vertical_kb(
        callback_data=TeacherCD,
        text_template=TEXT_TEMPLATES["choose_teacher"],
        values=found,
    )
    await message.answer(text=TEXT["choose_teacher"], reply_markup=kb, parse_mode=ParseMode.HTML)


@router.callback_query(TeacherCD.filter())
async def teacher_finish(query: CallbackQuery, state: FSMContext, callback_data: TeacherCD, session: AsyncSession):
    await query.answer()

    await state.update_data(teacher=callback_data.value)
    data = await state.get_data()

    print(f"Teacher registration finished: \n{data}") # TODO: Delete

    text = teacher_finish_text(data["teacher"])
    await query.message.edit_text(text=text, parse_mode=ParseMode.HTML)

    await state.clear()

    # TODO: get lecturer_id from API
    await make_user_lecturer(session, query.from_user.id, lecturer_id=33)