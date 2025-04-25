from aiogram import Router
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode

router = Router()


@router.message()
async def any(msg: Message):

    await msg.answer("Не понимаю вас. Пожалуйста, используйте команды ниже👇\n\n/options - <i>Настройки уведомлений</i>", parse_mode=ParseMode.HTML)
