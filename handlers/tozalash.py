from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("delete"))
async def delete_message(message: Message):
    await message.delete()
    await message.answer("Xabar o'chirildi!")