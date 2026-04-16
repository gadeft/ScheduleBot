from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


KB_LIST = [
        [KeyboardButton(text="Yesterday"), KeyboardButton(text="Today"), KeyboardButton(text="Tomorrow")],
        [KeyboardButton(text="Previous week"), KeyboardButton(text="Current week"), KeyboardButton(text="Next week")],
        [KeyboardButton(text="Choose a day")],
    ]

def get_main_kb():
    keyboard = ReplyKeyboardMarkup(keyboard=KB_LIST, resize_keyboard=True, one_time_keyboard=False)
    return keyboard