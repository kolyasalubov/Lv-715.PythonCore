from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работи')
b2 = KeyboardButton('/Контакти')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделится номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).row(b2,b3)
