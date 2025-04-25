from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from functions import userDb_sqlite

from markups import start_markup


router = Router()

UserData = userDb_sqlite.UsersDatabase()


@router.message(Command("options"))
async def options(msg: Message):

    active = UserData.get_activity_user(msg.from_user.id)

    if active == "active":
        activity = "включены ✅"
        
    elif active == "inactive":
        activity = "отключены ❌"

    await msg.answer(f"⚙️ Настройка уведомлений:\n\n🔔 Уведомления: {activity}", reply_markup=start_markup.startM(active))


