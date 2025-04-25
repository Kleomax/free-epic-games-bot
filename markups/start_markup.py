from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def startM(activity: str):
    markup = InlineKeyboardBuilder()

    if activity == None:
        markup.row(InlineKeyboardButton(text="✅ Получать уведомления", callback_data="confirm"))
        markup.row(InlineKeyboardButton(text="❌ Отказаться от уведомлений", callback_data="reject"))

    elif activity == "active":
        markup.row(InlineKeyboardButton(text="❌ Отказаться от уведомлений", callback_data="reject"))

    elif activity == "inactive":
        markup.row(InlineKeyboardButton(text="✅ Получать уведомления", callback_data="confirm"))


    return markup.as_markup()