
# -*- coding: utf-8 -*-

import requests
import json
import time
import blue
import random
import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler, \
    RegexHandler, BaseFilter
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineQueryResultArticle, ParseMode,
                      InputTextMessageContent)
import os
from os import environ

import urllib

from urllib import request
from urllib import parse

import logging
import re
from uuid import uuid4
import logging

RISPOSTA, CIFRA, FINE = range(3)

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Lunga vita e prosperità!')


def unknownMessage(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Non so come aiutarti! Qui diventa cazzo!')


def consiglio(bot, update):
    consigliList = blue.listConsigli

    update.message.reply_text(random.choice(consigliList))


def cambio(bot, update):
    reply_keyboard = [['Abbastanza', 'Poco', 'Fondamentale']]
    update.message.reply_text(
        "Per tua fortuna ci sono io ad aiutarti! Aggiorno costantemente tutte le valute esistenti ogni 3,14 secondi! "
        "\n Scrivi /cancel per interrompere il processo e cadere in povertà! "
        "\n Adesso, dimmi quanto è utile questo cambio per te:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return RISPOSTA


def cifra(bot, update):
    user = update.message.from_user
    replyother_keyboard = [['Penso di si', 'Penso di no']]
    update.message.reply_text("Hmm, capisco! capisco! Ma dimmi, ci sono in ballo più di 10 euro?",
                              reply_markup=ReplyKeyboardMarkup(replyother_keyboard, one_time_keyboard=True))

    return CIFRA


def fine(bot, update):
    user = update.message.from_user
    update.message.reply_text("Non ne vale la pena! Tieni i soldi in tasca! Non pensarci mai più!"
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
    photoIsland = blue.photoIsland
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=photoIsland)


def quokka(bot, update):
    listquokkas = blue.listquokkas

    listquotes = blue.listquotes

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=random.choice(listquotes))
    bot.send_photo(chat_id=chat_id, photo=random.choice(listquokkas))


def anziani(bot, update):
    listaforismi = blue.listaforismi

    listafotoanziani = blue.listafotoanziani

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=random.choice(listaforismi))
    bot.send_photo(chat_id=chat_id, photo=random.choice(listafotoanziani))


def gatti(bot, update):
    listgatti = blue.listgatti
    listfotogatti = blue.listfotogatti


    urlz = requests.get("http://thecatapi.com/api/images/get?format=src&type=gif")
    
    ''' xml = urllib.request.urlopen(urlz)
    data = xml.read()
    xml.close() '''


    chat_id =  update.message.chat_id
    bot.send_message(chat_id=chat_id, text=random.choice(listgatti))
    bot.send_video(chat_id=chat_id, video=urlz.url)



    '''random.choice(listfotogatti)'''

def inlinequery(bot, update):
    query = update.inline_query.query
    fineZ = blue.listInlineBotFrasiTrasform
    if not query:
        return

    results = list()

    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='SCRIVI IN CAPSLOCK E PREDOMINA!',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )

    '''  if "rotto" in query:

        risultato = random.choice(blue.listInlineBotLamentela)

    elif "saccenza" in query:

        risultato = random.choice(blue.listInlineBotSaccenza)

    else:
        risultato = random.choice(blue.listInlineBotFrasiTrasform) '''


    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title = 'Dillo con parole mie!',
            input_message_content=InputTextMessageContent(random.choice(fineZ))
        )
    )

    update.inline_query.answer(results)


def frasiFatte(bot, update):
    listCreaeFraseUno = blue.listCreateFraseUno
    listCreaeFraseDue = blue.listCreateFraseDue
    listCreaeFraseTre = blue.listCreateFraseTre
    listCreaeFraseQuattro = blue.listCreateFraseQuattro
    listCreaeFraseCinque = blue.listCreateFraseCinque
    listcreaeFraseSei = blue.listCreateFraseSei

    update.message.reply_text(random.choice(listCreaeFraseUno)
                                                + " "
                                                +random.choice(listCreaeFraseDue)
                                                + " "
                                                +random.choice(listCreaeFraseTre)
                                                + " "
                                                +random.choice(listCreaeFraseQuattro)
                                                + " "
                                                +random.choice(listCreaeFraseCinque)
                                                + " "
                                                +random.choice(listcreaeFraseSei))



def main():
    updater = Updater("322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("consiglio", consiglio))
    '''dp.add_handler(MessageHandler(Filters.text, unknownMessage))'''
    dp.add_handler(InlineQueryHandler(inlinequery))
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
    dp.add_handler((CommandHandler("quokkas", quokka)))
    dp.add_handler((CommandHandler("schlingel", gatti)))
    dp.add_handler((CommandHandler("hotelcantiere", anziani)))
    dp.add_handler((CommandHandler("frasifatte", frasiFatte)))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
