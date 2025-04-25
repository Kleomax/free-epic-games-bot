
import json

from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode


from functions import userDb_sqlite
from functions.epic_parser import get_games
from functions import formatter

from markups import game_markup


UserData = userDb_sqlite.UsersDatabase()

router = Router()


@router.message(F.text == "⏳ Ближайшие раздачи")
async def nearest_gifts(msg: Message):
    with open("games.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    
    for game in data:
        title = game[0]

        start_date = game[1]
        end_date = game[2]

        price = game[3]

        link = game[4]

        text = f"<b>📌 Название: {title}</b>\n\n<i>🏷️ Цена без скидки: {price}</i>\n\n<b><i>🎁 Начало раздачи: {await formatter.format_date(start_date)}</i></b>\n<b><i>📅 Конец раздачи: {await formatter.format_date(end_date)}</i></b>"

        await msg.answer_photo(photo=game[5], caption=text, parse_mode=ParseMode.HTML, reply_markup=game_markup.startM(link))
