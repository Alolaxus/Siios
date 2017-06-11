import requests
import json
import time
import random
import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler
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

def unknownMessage(bot, update):
    update.message.reply_text('Non so come aiutarti! Qui diventa cazzo!')


def consiglio(bot, update):
    listConsigli = ["Apri un Blog!", "Convinci qualcuno a finanziarti!", "Prendi un dottorato!",
                    "Non so aiutarti! Qui diventa cazzo!",
                    "Paga le tue multe!", "Fai una maratona di Gazebo!", "Sfogati con un cameriere!"]
    update.message.reply_text(random.choice(listConsigli))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater('322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("consiglio", consiglio))
    dp.add_handler(MessageHandler("suca", unknownMessage()))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


