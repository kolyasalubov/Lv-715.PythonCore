from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Смачного', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напишіть боту в ЛС:\nhttps://t.me/Sushi_FreshBot')


# @dp.message_handler(commands=['Режим_работы'])
async def sushi_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Нд-Чт с 9:00 до 20:00, Пя-Сб с 10:00 до 23:00', reply_markup=kb_client)
# @dp.message_handler(commands=['Pасположение'])
async def sushi_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вул. Чорновола 12', reply_markup=kb_client)

@dp.message_handler(commands=['Меню'])
async def sushi_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(sushi_open_command, commands=['Режим_работи'])
    dp.register_message_handler(sushi_place_command, commands=['Контакти'])
    dp.register_message_handler(sushi_menu_command, commands=['Меню'])