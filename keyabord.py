from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from glob import glob

startKeyboard = InlineKeyboardMarkup()
startKeyboard.insert(InlineKeyboardButton('Привет', callback_data='start'))

cardsKeyboard = InlineKeyboardMarkup()
mycards = glob('./cards/*.encrypted')
for lastDigits in mycards:
    lastDigits = lastDigits[8:12]
    cardsKeyboard.insert(InlineKeyboardButton(f'*{lastDigits}', callback_data=f'*{lastDigits}'))

codeKeyboard = InlineKeyboardMarkup()
codeKeyboard.insert(InlineKeyboardButton('Получить код', callback_data='get_code'))