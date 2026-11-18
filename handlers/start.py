from aiogram import types, filters, Router
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message):
    await msg.answer("xush kelibsiz!")
    await msg.answer("siz start bosdingiz\n bot kamandalari")
    await msg.answer("/delete")
    await msg.answer("/kuchuk")
    await msg.answer("/mashina")



