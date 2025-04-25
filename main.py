import sys
import asyncio
import logging
import fontstyle
import multiprocessing

from aiogram import Dispatcher

from config import bot

from handlers import start_handler, options, any_message, main_menu_handler
from handlers.admin import statistics
from handlers.test import worker, router

async def main():

    process = multiprocessing.Process(target=worker)
    process.start()

    # в proxy указан прокси сервер pythonanywhere, он нужен для подключения
    dp = Dispatcher(maintenance_mode=False)

    dp.include_routers(
        start_handler.router,
        router,
        options.router,
        main_menu_handler.router,
        statistics.router,
        any_message.router
    )

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        print(fontstyle.apply("[+] Бот запущен", "bold/Italic/green"))
        print(fontstyle.apply("[INFO] Для остановки бота нажмите сочетание клавиш: ctrl + c", "italic/yellow"))

        logging.basicConfig(level=logging.INFO, stream=sys.stdout)

        asyncio.run(main())

    except KeyboardInterrupt:
        print(fontstyle.apply("[-] Бот Остановлен", "bold/Italic/red"))
