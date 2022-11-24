from aiogram import types, Dispatcher
from create_bot import dp

# @dp.message_handler() ## Текст в телеграмі
async def echo_bot(message: types.Message):
    if message.text == 'Привіт':
        await message.answer('Доброї ночі')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_bot)