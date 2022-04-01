import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2101483046:AAFWSPsPh3ZMnK1Oegxs_z0Eg0a5D1xtBnc'

wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom Xush kelibsiz")



@dp.message_handler()
async def natija(message: types.Message):
   try:
       qid=wikipedia.summary(message.text)
       await message.answer(qid)
   except:
       await message.answer('Bunday maqola mavjud emas.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)