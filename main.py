import envs
import logging
from asyncio import sleep

from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
from aiogram.utils.markdown import text, bold

import keyabord as kb
from card import Card
from imap import Mail


logging.basicConfig(level=logging.INFO)
bot = Bot(token=envs.API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    status = await bot.get_chat_member(-1001631976127, msg.from_user.id)
    print(status)
    if (status.status != 'left'):
        await msg.answer('Выберите карту: ', reply_markup=kb.cardsKeyboard)
    else:
        pass

@dp.message_handler(commands=['code'])
async def code(msg: types.Message):
    status = await bot.get_chat_member(-1001631976127, msg.from_user.id)
    print(status)
    if (status.status != 'left'):
        await msg.answer('Проверить есть ли код?', reply_markup=kb.codeKeyboard)
    else:
        pass

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('*'))
async def processCards(call: types.CallbackQuery):
    lastDigits = call.data[1:]
    card = Card(lastDigits=lastDigits)
    card.decrypt()
    info = text(
        bold('Number: '),
        (f'`{card.number}`\n\n'),
        bold('Date: '),
        (f'`{card.date}`\n\n'),
        bold('CVV: '),
        (f'`{card.cvv}`'),
        sep=''
    )
    await call.message.edit_text(info, parse_mode=types.ParseMode.MARKDOWN, reply_markup=kb.codeKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'get_code')
async def getCode(call: types.CallbackQuery):
    await call.message.edit_text('Получаю код проверки...')
    mail = Mail()
    for i in range(5):
        await sleep(2)
        if (mail.searchUnseen()[0] != b''):
            code = text(
                (f'`{mail.getCode()}`'),
                sep=''
                )
            reply = None
            print('Соединение закрыто')
            break
        else:
            if i != 4:
                code = text(
                    (f'Получение кода... ({i+1}/5)'),
                    sep=''
                )
                await call.message.edit_text(code)
            else:
                code = text(
                    ('Код не получен'),
                    sep=''
                )
                reply = kb.codeKeyboard
    mail.close()
    mail.logout()
    print('соединение закрыто основательно')
    await call.message.edit_text(code, parse_mode=types.ParseMode.MARKDOWN, reply_markup=reply)


async def on_startup(dp):
    logging.warning('Starting webhook..')
    await bot.set_webhook(envs.WEBHOOK_URL, drop_pending_updates=True)
async def on_shutdown(dp):
    logging.warning('Shutting down..')
    logging.warning('Bye!')
start_webhook(
    dispatcher=dp,
    webhook_path=envs.WEBHOOK_URL_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host=envs.WEBAPP_HOST,
    port=envs.WEBAPP_PORT,
)

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
