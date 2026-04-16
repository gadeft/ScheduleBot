from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_vertical_kb(
        callback_data: CallbackData,
        text_template: str,
        values: list,
        *static_values
) -> InlineKeyboardMarkup:

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=text_template.format(i, *static_values),
                callback_data=callback_data(value=i).pack()
            )]
            for i in values
        ]
    )

    return kb