from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привет!")], [KeyboardButton(text="Как дела?")],
            [KeyboardButton(text="Пока!")]
        ],
        resize_keyboard=True
    )
    return keyboard


def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Узнать погоду", callback_data="button_pressed")]
        ],
    )
    return keyboard



