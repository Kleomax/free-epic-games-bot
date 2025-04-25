from aiogram import Router, F
from aiogram.types import Message

from filters.admin_filter import IsAdmin

from functions.userDb_sqlite import UsersDatabase

from config import admins_list


router = Router()

router.message.filter(IsAdmin(admins_list))

UserData = UsersDatabase()


@router.message(F.text == "📊 Статистика")
async def get_statics(msg: Message):

    all_users = UserData.get_users()
    activity_users = UserData.get_activity_users()

    await msg.answer(f"Общее кол-во пользователей: {len(all_users)}\nКол-во активных пользователей: {len(activity_users)}")
