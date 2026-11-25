from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def xabar(message: Message):
    sana = message.forward_origin.date
    await message.answer(str(sana))