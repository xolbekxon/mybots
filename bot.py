import logging
from transliterate import to_cyrillic, to_latin
from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord

API_TOKEN = '2114921627:AAHPMv1SHZdu5tdtXMT6dMVnJOLM2LEiJ-s'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Imlolar Botiga Xush Kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = to_cyrillic(message.text)
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(to_latin(response))
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)