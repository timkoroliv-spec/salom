from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import random

router = Router()

rasmlar = [
    "https://zoonika.com/porodi-sobak/alyaskinskij-malamut.html",
    "https://birbir.uz/ru/chirchik/cat/zhivotnyye/sobaki/o/xaski-kuchuk-khaski-kuchuk-219867942",
    "https://odam.uz/kuchuklar-haqida-keng-tarqalgan-7-ta-afsona/",
    "https://www.rokform.com/blogs/rokform-blog/iphone-18-release-date?srsltid=AYCX9vJWwMVY0khHPUcmOHF17oGEpM0yPfQl-jv8SOVk6QZr9oH0sMED",
    "https://kun.uz/news/2016/09/10/dunedagi-eng-havfli-ajvonlar-rujhati-elon-kilindi",
]

@router.message(Command("kuchuk"))
async def answer_photo(message: Message):
    rasm = random.choice(rasmlar)

    await message.answer_photo(
        photo=rasm,
        caption="Mana sizga kuchuk rasmi"
    )