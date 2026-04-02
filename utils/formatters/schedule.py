from datetime import datetime
from datetime import timedelta


NUMERATION = {
    "09:00": "1 ПАРА",
    "10:30": "2 ПАРА",
    "12:10": "3 ПАРА",
    "13:40": "4 ПАРА",
    "15:10": "5 ПАРА",
    "16:30": "6 ПАРА",
}

TIME_FORMAT = "%H:%M"
LESSON_DURATION_MINUTES = 80


def format_lessons(data: list):
    result = ""
    for lesson in data:
        start_time = data[lesson]["time_start"]
        end_time = data[lesson]["time_end"]
        lecturer = data[lesson]["lecturer"]
        url = data[lesson]["url"]
        venue = data[lesson]["venue"]

        result += (f"{NUMERATION[start_time]}             {start_time} - {end_time}\n"
                   f"{lesson.upper()}\n"
                   f"{lecturer}\n"
                   f"Посилання: {url}\n"
                   f"Кабінет: {venue}\n"
                   f"\n")

    return result


def day_lessons(lessons: list, day_name: str):
    result = f"<i>{day_name.upper()}</i>\n"
    result += format_lessons(lessons)
    result += "\n"
    return result


def today_lessons(data: list):
    if not data:
        return "No lessons for today."

    result = "<b>Lessons for today:</b>\n"
    result += format_lessons(data)
    return result


def tomorrow_lessons(data: list):
    if not data:
        return "No lessons for tomorrow."

    result = "<b>Lessons for tomorrow:</b>\n"
    result += format_lessons(data)
    return result


def yesterday_lessons(data: list):
    if not data:
        return "No lessons for yesterday."

    result = "<b>Lessons for tomorrow:</b>\n"
    result += format_lessons(data)
    return result


def week_schedule(days: list):
    result = "<b>Lessons for the week:</b>\n\n"

    for day in days:
        if day["lessons"]:
            result += day_lessons(day["lessons"], day["weekday"])

    return result


def specific_day_format():
    result = "Choose a day on the keyboard (if you don't see it click on the button with 4 dots near the emoji button)"
    return result