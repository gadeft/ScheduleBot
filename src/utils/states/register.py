from aiogram.fsm.state import StatesGroup, State


class RegisterSG(StatesGroup):
    search_teacher = State()