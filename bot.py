from cmath import asinh
from ctypes import resize
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton


from config import TOKEN, legend, latinizator


logging.basicConfig(filename = 'log.log', level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    text = f'Привет, {user_name} \n введи свое имя и свою фамилию на кирилице \n А и я переведу их в латиницу\n Eсли запутался нажми /help'
    user_id = message.from_user.id
    logging.info(f'{user_name} {user_id} send message {message.text}')
    await message.reply(text, reply_markup=kb_client)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    text = f'дорогой, {user_name} начни вводить имя и фамилию на кирилице и я переведу ее в латиницу.\n\n\nОбрати внимание что я сделаю все первые буквы заглавными'
    user_id = message.from_user.id
    logging.info(f'{user_name} {user_id} send message {message.text}')
    await message.reply(text)


@dp.message_handler()
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    text = ' '.join([i.capitalize() for i in latinizator(message.text, legend).split()])
    # print(''.join([i.capitalize() for i in (x.lower().split())]))
    user_id = message.from_user.id
    logging.info(f'{user_name} {user_id} send message {message.text}')
    await message.reply(text)

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1,b2)


if __name__ == '__main__':
    executor.start_polling(dp)

















