
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def aniqlash(message: Message):
    origin = message.forward_origin

    if origin and origin.type == "user":
        user = origin.sender_user

        await message.answer(
            f"Ismi: {user.first_name}\n"
            f"ID: {user.id}\n"
            f"Vaqti: {origin.date}"
        )

    elif origin and origin.type == "channel":
        chat = origin.chat

        await message.answer(
            f"Kanal/Guruh: {chat.title}\n"
            f"ID: {chat.id}\n"
            f"Vaqti: {origin.date}"
        )

    else:
        await message.answer("Ma'lumot topilmadi!")

