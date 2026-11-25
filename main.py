import asyncio, logging
from aiogram import Bot, Dispatcher
from config.settings import token
from handlers.start import rt as start
from handlers.aniqla import router as aniqla
from handlers.vaqt import router as vaqt
from handlers.all import rt as all


dp = Dispatcher()

async def main():
    bot = Bot(token)
    dp.include_router(start)
    dp.include_router(aniqla)
    dp.include_router(vaqt)
    dp.include_router(all)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
