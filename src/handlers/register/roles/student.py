from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from src.utils.keyboards.register import get_vertical_kb
from src.utils.callbacks.register import FacultyCD, CourseCD, GroupNumberCD
from src.utils.formatters.register import (
    TEXT, TEXT_TEMPLATES, FACULTIES, COURSES, GROUPS_PER_COURSE, student_finish_text
)
from src.loader import db


router = Router()


async def choose_faculty(message: Message, state: FSMContext):
    kb = get_vertical_kb(
        callback_data=FacultyCD,
        text_template=TEXT_TEMPLATES["faculty"],
        values=FACULTIES
    )
    await message.answer(text=TEXT["choose_faculty"], reply_markup=kb, parse_mode=ParseMode.HTML)


@router.callback_query(FacultyCD.filter())
async def choose_course(query: CallbackQuery, state: FSMContext, callback_data: FacultyCD):
    await query.answer()
    await state.update_data(faculty=callback_data.value)

    kb = get_vertical_kb(
        callback_data=CourseCD,
        text_template=TEXT_TEMPLATES["course"],
        values=COURSES
    )
    await query.message.edit_text(text=TEXT["choose_course"], reply_markup=kb, parse_mode=ParseMode.HTML)


@router.callback_query(CourseCD.filter())
async def choose_group(query: CallbackQuery, state: FSMContext, callback_data: CourseCD):
    await query.answer()

    await state.update_data(course=callback_data.value)
    data = await state.get_data()

    kb = get_vertical_kb(
        GroupNumberCD,
        TEXT_TEMPLATES["group"],
        GROUPS_PER_COURSE,
        data["faculty"],
        data["course"]
    )
    await query.message.edit_text(text=TEXT["choose_group"], reply_markup=kb, parse_mode=ParseMode.HTML)


@router.callback_query(GroupNumberCD.filter())
async def student_finish(query: CallbackQuery, state: FSMContext, callback_data: GroupNumberCD):
    await query.answer()

    await state.update_data(group=callback_data.value)
    data = await state.get_data()

    print(f"Student registration finished: \n{data}") # TODO: Delete

    text = student_finish_text(data["faculty"], data["course"], data["group"])
    await query.message.edit_text(text=text, parse_mode=ParseMode.HTML)

    await state.clear()

    await db.upsert_student(telegram_id=query.message.chat.id, group_id=10) # TODO: get group_id from API