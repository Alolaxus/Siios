# -*- coding: utf-8 -*-

import requests
import json
import time
import random
import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler, \
    RegexHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import logging
import re
from uuid import uuid4
import logging

RISPOSTA, CIFRA, FINE = range(3)

URL = "https://api.telegram.org/bot322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0/"
bot = telegram.Bot('322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Lunga vita e prosperità!')


def unknownMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Non so come aiutarti! Qui diventa cazzo!')


def consiglio(bot, update):
    listConsigli = ["Apri un Blog!", "Convinci qualcuno a finanziarti!", "Parla solo con chi ha almeno un dottorato!",
                    "Non andare a bobbonellare dopo le 23! MAI!", "Suona un brano di De Gregori!",
                    "Guarda solo il tg di Mentana!",
                    "Non vale la pena comprare dall'estero se non c\'e\' cambio favorevole!",
                    "Meno features = meno problemi!", "Prima di tutto chiediti: posso farlo col Mac?",
                    "Non stare a meno di 20 cm di distanza dalle altre persone!",
                    "Da quanto non vai a fare una scarpinata a Monte Pellegrino???",
                    "Copiare da uno solo è reato. Copiare da tanti è ricerca!", "Soltanto un Sith vive di assoluti!",
                    "Non c\'è provare...C\'è fare o non fare!", "Un vulcaniano non sarebbe mai così indeciso!",
                    "Vivi la vita un quarto di euro alla volta!",
                    "Scriviti tutti i tuoi conti!",
                    "Fai una maratona di Gazebo!", "Sfogati con un cameriere!"]
    update.message.reply_text(random.choice(listConsigli))


def cambio(bot, update):
    reply_keyboard = [['Abbastanza', 'Poco', 'Fondamentale']]
    update.message.reply_text(
        "Per tua fortuna ci sono io ad aiutarti! Aggiorno costantemente ogni valuta esistente ogni "
        "0.007 secondi! "
        "\n Scrivi /cancel per interrompere il processo e cadere in povertà! "
        "\n Adesso, dimmi quanto è utile questo cambio per te:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return RISPOSTA


def cifra(bot, update):
    user = update.message.from_user
    replyother_keyboard = [['Penso di si', 'Penso di no']]
    update.message.reply_text("Hmm, capisco! Ma dimmi, ci sono in ballo più di 10 euro?",
                              reply_markup=ReplyKeyboardMarkup(replyother_keyboard, one_time_keyboard=True))

    return CIFRA


def fine(bot, update):
    user = update.message.from_user
    update.message.reply_text("Amico mio, credimi, non ne vale la pena! Tieni i soldi in tasca!"
                              "\n\n FINE DELL\'OPERAZIONE!", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Bravo! Hai appena fatto un passo in più verso la classe operaia!',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def sendisland(bot, update):
    update.message.reply_text(
        photo="http://www.vladi-private-islands.de/fileadmin/_processed_/1/7/csm_cousine_island_057_1339e09652.jpg")


def main():
    updater = Updater('322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("consiglio", consiglio))
    '''dp.add_handler(MessageHandler(Filters.text, unknownMessage))'''

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("cambiomoneta", cambio)],

        states={
            RISPOSTA: [RegexHandler('^(Abbastanza|Poco|Fondamentale)$', cifra)],

            CIFRA: [RegexHandler('^(Penso di si|Penso di no)$', fine), MessageHandler(Filters.text, fine)]
        },

        fallbacks=[CommandHandler("cancel", cancel)]
    )
    dp.add_handler(conv_handler)
    dp.add_handler((CommandHandler("isola", sendisland)))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
