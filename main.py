from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = AsyncTeleBot('6230652323:AAF9g4bBcM_PCHdftL4QwGj7CFZNYjgyQ4A')



@bot.message_handler(commands=['help', 'start'])
async def sendWelcom(message):
    chat_id = message.from_user.id
    list_buttons = {'1':'1','2':'2'}
    await bot.send_message(chat_id, 'первый вариант', reply_markup=generate_btns_under_line(list_buttons))

def generate_btns_under_line(name_signal):
    markup = InlineKeyboardMarkup()
    buttons = []
    for i in name_signal.keys():
        buttons.append(InlineKeyboardButton(i, callback_data=name_signal[i]))
    markup.add(*buttons)
    return (markup)

'''
async def sendWelcom(message):
    chat_id = message.from_user.id
    
    await bot.send_message(chat_id, 'gdf')
    await bot.send_video(chat_id, 'https://www.youtube.com/watch?v=g0Ki_352rJg')
    await bot.send_photo(chat_id, 'https://images.thevoicemag.ru/upload/img_cache/d86/d8619b2cc66f72ac1ce5582fe6f3805e_cropped_666x833.jpg', caption="Как тебе?")
    await bot.send_document(chat_id, open('text.txt', 'rb'))
    await bot.send_sticker(chat_id,'CAACAgIAAxkBAAIiUGSkDGckyBhLSrARgpw8T3cN2whqAALDEgACvR5hS6hEpeGsurpNLwQ')
    await bot.reply_to(message, 'Здорова')
    
async def sendWelcom(message):
    chat_id = message.from_user.id
    list_buttons = ['1','2','3']
    await bot.send_message(chat_id, 'ТтттттттттттттТ', reply_markup=generate_btns(list_buttons, 2))

def generate_btns(list_butonns, rows):
    markup = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
    markup.add(*list_butonns, row_width=rows)
    return (markup)

93б
'''

@bot.message_handler(commands=['weather'])
async def weather(message):
    await bot.reply_to(message, 'Ну и погода у тебя в захалустьи... Хорошо, что я на Бали!')

@bot.message_handler(commands=['test'])
async def test(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Проверка связи', disable_notification=True, protect_content=True)

@bot.message_handler(commands=['dice'])
async def test(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎲')
    print(bot_message.dice.value)

#@tg_sticker_id_bot
#@tg_sticker_id_bot

@bot.message_handler(commands=['kazino'])
async def test(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎰')
    print(bot_message.dice.value)


@bot.message_handler(func=lambda message: True)
async def draznit(message):
    print(message)
    text_message = message.text.lower()
    answer = None
    for i in ['шут', 'юмор', 'смех', 'смеш', 'анекдот']:
        if i in text_message:
            answer = 'Ха ха! Снайпер чихнул'
            await bot.reply_to(message, answer)
    if answer == None:
        if 'дел' in text_message or 'настро' in text_message and answer==None:
            await bot.send_message(message, 'Бомба.')
        else:
            await bot.send_message(message, 'Поддерживаю.')


import asyncio
asyncio.run(bot.polling())
