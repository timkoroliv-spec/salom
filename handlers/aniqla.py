
from aiogram import Router
from aiogram.types import Message
from datetime import timezone, timedelta

router = Router()

uzbekiston = timezone(timedelta(hours=5))


@router.message()
async def aniqlash(message: Message):
    origin = message.forward_origin

    if origin and origin.type == "user":
        user = origin.sender_user
        vaqt = origin.date.astimezone(uzbekiston).strftime(
            "%Y-yil %B %d-kun %H:%M:%S"
        )

        await message.answer(
            f"Ismi: {user.first_name}\n"
            f"ID: {user.id}\n"
            f"Yuborilgan vaqti: {vaqt}"
        )

    elif origin and origin.type == "channel":
        chat = origin.chat
        vaqt = origin.date.astimezone(uzbekiston).strftime(
            "%Y-yil %B %d-kun %H:%M:%S"
        )

        await message.answer(
            f"Kanal/Guruh: {chat.title}\n"
            f"ID: {chat.id}\n"
            f"Yuborilgan vaqti: {vaqt}"
        )

    else:
        await message.answer("Ma'lumot topilmadi!")
