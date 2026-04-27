from datetime import date

from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
import requests

from src.utils.formatters.schedule import *
from src.utils.parser import parser

router = Router()

DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

@router.message(Command("week"))
async def week(message: types.Message):
    resp = requests.get("http://localhost:8000/schedule/week") # TODO create service which gets the data from api and move it there
    data = resp.json()

    answer = week_schedule(data["week_schedule"])

    await message.answer(answer, parse_mode=ParseMode.HTML)


@router.message(Command("today"))
async def today(message: types.Message):
    today_weekday = date.today().isoweekday()

    # user_data = db.get_by_id(message.from_user.id)

    # raw_data = await get_schedule(day_id=today_weekday, week_id=2, group_id=8)
    # parsed_data = parser.parse(raw_data)
    answer = today_lessons(parsed_data["ІПЗ-32"][2]["Четвер"]) # TODO: take data from database according user id

    await message.answer(answer, parse_mode=ParseMode.HTML)


@router.message(Command("tomorrow"))
async def tomorrow(message: types.Message):
    now = date.today()
    tomorrow_day = now + timedelta(days=1)
    tomorrow_day_name = tomorrow_day.strftime("%A").lower()

    resp = requests.get(f"http://localhost:8000/schedule/{tomorrow_day_name}")
    data = resp.json()

    answer = tomorrow_lessons(data["lessons"])

    await message.answer(answer, parse_mode=ParseMode.HTML)


@router.message(Command("yesterday"))
async def yesterday(message: types.Message):
    now = date.today()
    yesterday_day = now - timedelta(days=1)
    yesterday_day_name = yesterday_day.strftime("%A").lower()

    resp = requests.get(f"http://localhost:8000/schedule/{yesterday_day_name}")
    data = resp.json()

    answer = yesterday_lessons(data["lessons"])

    await message.answer(answer, parse_mode=ParseMode.HTML)