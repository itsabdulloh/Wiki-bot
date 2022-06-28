import asyncio
import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5040399767:AAGmsC_S8vjAbHXxQxgRH6JkmcI4pfQP-M'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token='5040399767:AAGmsC_S8vjAbHXxQxgRH6JkmcI4pfQP-M8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # await message.reply(f"Assalomu alaykum {message.from_user.full_name}, Wikipeida Botiga Xush Kelibsiz!")


@dp.message_handler()
async def sendWiki(message: types.Message):
    await asyncio.sleep(1)

    await types.ChatActions.typing()

    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)