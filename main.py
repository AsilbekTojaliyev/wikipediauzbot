import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from wikipedia import wikipedia

bot = Bot(token="7232522170:AAFdHMbIdAXlfnuNmfRZhkH5mAu_BjeiE5Y")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(mg: Message):
    if mg.from_user.username:
        await mg.answer(f"salom {mg.from_user.username}, botga xush kelibsiz!!!")
    else:
        await mg.answer(f"salom {mg.from_user.first_name} botga xush kelibsiz!!!")
    await mg.answer("botdan foydalanish uchun istalgan maqola nomini kiriting.")


@dp.message()
async def wikiped(mg: Message):
    try:
        wikipedia.set_lang("uz")
        text = wikipedia.summary(mg.text)
        await mg.answer(text)
    except:
        await mg.answer("bunday maqola mavjud emas")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
