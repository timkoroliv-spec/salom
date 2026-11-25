from aiogram import types, filters, Router
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message):
    await msg.answer("xush kelibsiz!")
    await msg.answer("siz start bosdingiz")



