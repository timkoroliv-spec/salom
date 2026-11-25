from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def xabar(message: Message):
    origin = message.forward_origin

    if origin and origin.type == "user":
        ism = origin.sender_user.first_name
        id = origin.sender_user.id

        await message.answer(f"Ismi: {ism}\nID: {id}")
    else:
        await message.answer("Ism topilmadi!")