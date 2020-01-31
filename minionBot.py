#!/usr/bin/env python
import telebot
import time
import requests
from telebot.types import Message
from telebot.types import Chat

SPACE = "---------------------------------------------------------------------------------------------------------------"
# https://api.telegram.org/bot<token>/getUpdates
TOKEN = '1040218815:AAF4u8NO6K9MZ5LdqSI-lXLV3P4atRUEFsE'
# https://api.telegram.org/bot1040218815:AAF4u8NO6K9MZ5LdqSI-lXLV3P4atRUEFsE/getUpdates
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
chat_id = -1001438462873
i = 0


# while i < 5:
#     payload = {
#         'chat_id': 701251792,
#         'text'   : f"{i}"
#         }
#     r = requests.post(f'{MAIN_URL}/sendMessage', data=payload)
#     i = i + 1
#     print(i)
def find_at(msg):
    result = ""
    for text in msg:
        if '!!!' not in text:
            result = result + " " + text
    return result


bot = telebot.TeleBot(TOKEN)

print("Start")


@bot.message_handler(content_types=['text'])
def send_to_group_from(message: Message):
    # if "!!!" in message.text:
    #     print("I am runing")
    #     texts = message.text.replace('!!!', '').strip()
    #     t = "Someone said:\n" + texts
    #     bot.send_message(chat_id=chat_id, text=t)
    #     bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    import math
    try:
        ev = eval(message.text)
    except:
        ev = "Can't evaluate your message"

    # bot.send_message(chat_id=chat_id, text=ev)
    bot.reply_to(message=message, text=ev)
    # bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)
