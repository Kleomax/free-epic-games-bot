from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def startM(url: str):
    markup = InlineKeyboardBuilder()

    markup.row(InlineKeyboardButton(text="Перейти", url=url))

    return markup.as_markup()
