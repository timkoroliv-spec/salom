from aiogram import Router, types

rt = Router()
@rt.message()
async def test_handler(msg: types.Message):
    await msg.reply("hello")
    print(msg.from_user.id)
    await msg.forward(9281955487)
