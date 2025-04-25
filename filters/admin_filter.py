from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):
    def __init__(self, admins_list: list[int]) -> None:
        self.__admins_list = admins_list

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.__admins_list
