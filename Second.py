import requests
import json
import time
import random
import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
import re
from uuid import uuid4
import logging

URL = "https://api.telegram.org/bot322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0/"
bot = telegram.Bot('322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def consiglio(bot, update):
    listConsigli = ["Apri un Blog!", "Non e' difficile, e' inutile!", "Prendi un dottorato!",
                    "Non so aiutarti! Qui diventa cazzo!",
                    "Paga le tue multe!"]
    update.message.reply_text(random.choice(listConsigli))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater('322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("consiglio", consiglio))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


'''
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def consiglio(bot, update):
    listConsigli = ["Apri un Blog!", "Non e' difficile, e' inutile!", "Prendi un dottorato!",
                    "Non so aiutarti! Qui diventa cazzo!",
                    "Paga le tue multe!"]
    update.message.reply_text("Ciao!")


def main():
    updater = Updater("322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0")
    bot = telegram.Bot(token='322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("consiglio", consiglio))
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()

    updater.idle()

    if __name__ == '__main__':
        main()
'''

'''
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


text, chat = get_last_chat_id_and_text(get_updates())

def main():
    last_textchat = (None, None)
    listConsigli = ["Apri un Blog!", "Non e' difficile, e' inutile!", "Prendi un dottorato!",
                    "Non so aiutarti! Qui diventa cazzo!",
                    "Paga le tue multe!"]


    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:
            if text == "come va":
                send_message("bene", chat)
            elif text == "suca":
                send_message("milla", chat)
            elif text == '/consiglio':
                send_message(random.choice(listConsigli), chat)

            else:
                send_message("non ho capito", chat)

            last_textchat = (text, chat)
        time.sleep(0.5)


if __name__ == '__main__':
        main()
        '''
