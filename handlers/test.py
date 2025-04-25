import datetime
import asyncio
import json
import time
import fontstyle

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError, TelegramRetryAfter

from functions import userDb_sqlite
from functions.epic_parser import get_games
from functions import formatter

from markups import game_markup, statistics_markup

from config import bot


UserData = userDb_sqlite.UsersDatabase()

router = Router()


@router.callback_query()
async def test1(call: CallbackQuery):
    if call.data == "confirm":

        if UserData.user_exists(call.from_user.id) == True:
            UserData.set_activity(call.from_user.id, "active")
        else:
            UserData.add_user(call.from_user.id, "active")

        await call.message.answer("<i>Вы успешно подписались на получение новостей о раздаче игр ✅</i>", parse_mode=ParseMode.HTML, reply_markup=statistics_markup.MainMenu(call.from_user.id))

    elif call.data == "reject":

        if UserData.user_exists(call.from_user.id) == True:
            UserData.set_activity(call.from_user.id, "inactive")
        else:
            UserData.add_user(call.from_user.id, "inactive")

        await call.message.answer("Вы отказались от получения новостей о раздаче игр 😔", reply_markup=statistics_markup.MainMenu(call.from_user.id))

    return

async def scheduler():

    while True:

        if datetime.datetime.now().strftime('%H:%M') == "18:00":
            
            games = get_games()

            with open('games.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            for game in games:

                if game[1] == str(datetime.datetime.now().date()):
                    title = game[0]

                    start_date = game[1]
                    end_date = game[2]

                    print(end_date)

                    price = game[3]

                    link = game[4]

                    text = f"🥳 НАЧАЛАСЬ РАЗДАЧА <b><i>{title}</i></b>\n\n<b><i>🎁 Начало раздачи: {await formatter.format_date(start_date)}</i></b>\n<b><i>📅 Конец раздачи: {await formatter.format_date(end_date)}</i></b>\n\nСкорее заходи и забирай 👇"

                    users = UserData.get_activity_users()

                    for user in users:
                        try:
                            await bot.send_photo(chat_id=int(user), photo=game[5], caption=text, parse_mode=ParseMode.HTML, reply_markup=game_markup.startM(link))

                        except TelegramForbiddenError as exc:
                            print(fontstyle.apply(exc, 'bold/Italic/yellow'))
                            UserData.set_activity(user, "inactive")

                            time.sleep(0.1)

                            continue

                        except TelegramBadRequest as exce:
                            print(fontstyle.apply(exce, 'bold/Italic/yellow'))
                            UserData.set_activity(user, "inactive")

                            time.sleep(0.1)

                            continue

                        except TelegramRetryAfter as ex:
                            await asyncio.sleep(ex.retry_after)

                            continue
            

            if games[0][0] != data[0][0]:

                users = UserData.get_activity_users()

                for user in users:
                    for game in games:
                        title = game[0]

                        start_date = game[1]
                        end_date = game[2]

                        price = game[3]

                        link = game[4]

                        text = f"<b>📌 Название: {title}</b>\n\n<i>🏷️ Цена без скидки: {price}</i>\n\n<b><i>🎁 Начало раздачи: {await formatter.format_date(start_date)}</i></b>\n<b><i>📅 Конец раздачи: {await formatter.format_date(end_date)}</i></b>"
                        
                        try:
                            await bot.send_photo(chat_id=int(user), photo=game[5], caption=text, parse_mode=ParseMode.HTML, reply_markup=game_markup.startM(link))
                        
                        except TelegramForbiddenError as exc:
                            print(fontstyle.apply(exc, 'bold/Italic/yellow'))
                            UserData.set_activity(user, "inactive")

                            time.sleep(0.1)

                            continue

                        except TelegramBadRequest as exce:
                            print(fontstyle.apply(exce, 'bold/Italic/yellow'))
                            UserData.set_activity(user, "inactive")

                            time.sleep(0.1)

                            continue

                        except TelegramRetryAfter as ex:
                            await asyncio.sleep(ex.retry_after)

                            continue

                with open('games.json', 'w', encoding='utf8') as file:
                    json.dump(games, file, indent=4, ensure_ascii=False)
                    
            else:
                pass


        await asyncio.sleep(50)

def worker():
    asyncio.run((scheduler()))
