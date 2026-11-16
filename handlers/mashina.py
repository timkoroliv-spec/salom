from aiogram import types, filters, Router
rt = Router()
@rt.message(filters.Command("mashina"))
async def mashina(msg: types.Message):
    await msg.answer("Mashinalar bolimiga xush kelibsiz!")
    await msg.answer("Bizdagi mashinalar")
    await msg.answer("Damas, Cobalt, Lasetti, Labo, Nexia")
    await msg.answer("BYD, Tesla, Li Auto")

