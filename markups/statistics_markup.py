from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import admins_list


def MainMenu(user_id: int):

    keyboard_btns = [
        [
            KeyboardButton(text="⏳ Ближайшие раздачи")
        ]
    ]

    if user_id in admins_list:
        keyboard_btns.insert(1, [KeyboardButton(text="📊 Статистика")])

    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_btns,
        resize_keyboard=True,
    )

    return keyboard
