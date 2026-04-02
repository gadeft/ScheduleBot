from datetime import date

import requests

from aiogram.fsm.state import StatesGroup, State

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import DialogManager, StartMode

from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums import ParseMode

from utils.formatters.schedule import day_lessons


DAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


class MySG(StatesGroup):
    calendar = State()


async def on_date_selected(
        callback,
        widget,
        manager: DialogManager,
        selected_date: date,
):
    group_id = manager.start_data["group_id"]
    weekday = DAYS.get(selected_date.weekday())

    resp = requests.get(f"http://localhost:8000/schedule/{weekday.lower()}")
    data = resp.json()

    text = day_lessons(data["lessons"], weekday)
    text += f"\n\n<b>Group ID: {group_id}</b>" # TODO: delete

    await callback.message.answer(text, parse_mode=ParseMode.HTML)
    await callback.message.delete()
    await manager.done()


dialog = Dialog(
    Window(
        Const("Choose a date"),
        Calendar(
            id="calendar",
            on_click=on_date_selected,
        ),
        state=MySG.calendar,
    )
)

router = Router()

@router.message(Command("specific_day"))
async def cmd_specific_day(message: Message, dialog_manager: DialogManager, group_id: int = None):
    data = {
        "group_id": group_id,
    }
    await dialog_manager.start(
        MySG.calendar,
        data=data,
        mode=StartMode.RESET_STACK,
    )