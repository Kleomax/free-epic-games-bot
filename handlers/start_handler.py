from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

from functions import userDb_sqlite

from markups import start_markup, statistics_markup

router = Router()

UserData = userDb_sqlite.UsersDatabase()


@router.message(Command("start"))
async def start(msg: Message):
    
    if UserData.user_exists(msg.from_user.id):
        await msg.answer("Вы уже зарегистрированы. Используйте команды ниже👇\n\n/options - <i>Настройка уведомлений</i>", parse_mode=ParseMode.HTML, reply_markup=statistics_markup.MainMenu(msg.from_user.id))
    
    else:
        await msg.answer("Привет 👋. Я бот, который умеет присылать уведомления о раздаче игр.\nДля того, чтобы подписаться на рассылку уведомлений, нажми кнопку ниже 👇", reply_markup=start_markup.startM(None))
    