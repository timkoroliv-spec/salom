from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def xabar(message: Message):
    origin = message.forward_origin

    if origin and origin.type == "channel":
        nomi = origin.chat.title
        id = origin.chat.id

        await message.answer(f"Chat: {nomi}\nID: {id}")
    else:
        await message.answer("Kanal yoki guruh topilmadi!")