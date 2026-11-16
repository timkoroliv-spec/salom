from aiogram import types, filters, Router
rt = Router()
@rt.message(filters.Command("qosim"))
async def start(msg: types.Message):
    await msg.answer("xush kelibsiz!")
    await msg.answer("siz start bosdingiz\nnima gap")
