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
                    "Mai andare a bobbonella dopo le 23!", "Impara un album di De Gregori e sarai al centro di ogni festa!",
                    "Il tg di Mentana è l'unico che ti dirà la verità!", "Non è spocchia ma amore per la conoscenza!"
                    "Solo nella chimica troverai la vera risposta!", "Genova non è una città ma uno stile di vita!"
                    "Meno features = meno problemi!", "Prima di tutto chiediti: posso farlo col Mac?",
                    "Non stare a meno di 20 cm di distanza dalle altre persone!", "La tua parola deve sempre prevalere in una discussione!",
                    "Trovati sempre qualcosa di diverso da fare, come Veltroni!",
                    "Da quanto non vai a fare una scarpinata a Monte Pellegrino???",
                    "Copiare da uno solo è reato. Copiare da tanti è ricerca!", "Soltanto un Sith vive di assoluti!",
                    "Non c\'è provare...C\'è fare o non fare!", "Un vulcaniano non sarebbe mai così indeciso!",
                    "Vivi la vita un quarto di euro alla volta!", "Basta mangiare! Sei malato!",
                    "Scriviti tutti i tuoi conti in un archivio cartaceo!",
                    "Lotta sempre contro le multinazionali, tranne Apple!",
                    "Piega perfettamente le camicie e mettile sempre nel cellophane!", "Non si può pagare con carta? No grazie!",
                    "Vuoi stupirla? Falle vedere che usi Ubuntu!", "Non ti finirà mai peggio del finale di Lost!",
                    "Non sentirti in colpa! Sono affari!",
                    "Non prendere mai decisioni prima di aver sorseggiato un Earl Grey!"
                    "Fai una maratona di puntate di Gazebo!", "Sfogati con un cameriere!"]
    update.message.reply_text(random.choice(listConsigli))


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
    listIslands = ["http://www.guoguiyan.com/data/out/105/68947604-island-wallpapers.jpg",
                   "http://www.vladi-private-islands.de/fileadmin/_processed_/1/7/csm_cousine_island_057_1339e09652.jpg",
                   "http://www.fregate.com/assets/stageImages/fregate-island-beaches1.jpg",
                   "http://andyflavoured.co.uk/wp-content/uploads/2012/01/Desert-Island.jpg",
                   "http://blog.idrsolutions.com/wp-content/uploads/2010/11/NATURE-FakaravaCoconutTree_1024x768.jpg",
                   "https://www.oen.org/wp-content/uploads/2015/05/Desert-Island_opt-1.jpg"
                   ]
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo="https://www.oen.org/wp-content/uploads/2015/05/Desert-Island_opt-1.jpg")


def quokka(bot, update):
    listquokkas = [
        "http://www.lastampa.it/rf/image_lowres/Pub/p4/2017/02/28/LaZampa/Foto/RitagliWeb/quokka01-10263-U11001522025659KVH-U11001522025659egE-1400x788%40LaStampa.it.JPG",
        "http://images2.corriereobjects.it/methode_image/2014/08/31/Scienze/Foto%20Gallery/BJsXlZIh1CJ-png__605.jpg",
        "https://s-media-cache-ak0.pinimg.com/originals/92/32/5c/92325cda58adb047c3215ef092874fb7.jpg",
        "https://s-media-cache-ak0.pinimg.com/originals/4d/43/8f/4d438f5ae4f70e4d1a5401f1bd4d2aac.jpg",
        "http://lepassionicondivise.altervista.org/wp-content/uploads/2016/10/uaa7Nzn.jpg",
        "https://s-media-cache-ak0.pinimg.com/736x/bb/7f/2f/bb7f2f4e470b07676817896aece18851.jpg",
    ]
    listquotes = ["Ho appena defecato!", "Ti piaccio perchè sorrido e ora sono a rischio di estinzione!",
                  "Apri la borsa e nutrimi, presto!", "Non mangio da 3 minuti!", "Ho il pelo morbido e pieno di malattie!",
                  "Sono davvero felice di vederti!", "Non sono mai sazio!",
                  "Sono il marsupiale più felice del mondo secondo i tuoi criteri!",
                  "Non posseggo alcuna ablilità per difendermi dai predatori!", "Ormai dipendo unicamente da te!",
                  "Sei il primo che si fa un selfie con me!"]

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=random.choice(listquotes))
    bot.send_photo(chat_id=chat_id, photo=random.choice(listquokkas))


def gatti(bot, update):

    listgatti = [
        "I gatti dormono da 16 a 18 ore al giorno. Ma il loro sonno è decisamente più leggero di quello degli esseri umani, per questo restano sempre vigili e pronti a reagire ad ogni stimolo.",
        "I gatti non possono percepire il sapore dolce. Provare a dividere il vostro cioccolato con loro sarebbe un gesto d’amore ben poco apprezzato.",
        "La maggioranza dei gatti bianchi con gli occhi azzurri è sorda. Quelli con un solo occhio azzurro sono sordi dal lato di quell’occhio, mentre i gatti bianchi con gli occhi gialli non manifestano questo problema.",
        "Ogni anno umano per un gatto corrisponde a circa sei anni di vita. Un micio di vent’anni sarebbe un rispettabile ultracentenario nel nostro mondo!",
        "La castrazione può estendere la durata delle loro vite di due o tre anni.",
        "I gatti apprezzano i suoni acuti, mentre i bassi gli risultano aggressivi e poco gradevoli.",
        "I gatti sono fermamente convinti di essere i padroni della casa in cui vivono. Gli umani sono solo coinquilini.",
        "I baffi servono ai gatti per misurare le distanze e sono in totale 24, raggruppati in unità da 4. Non si tratta di peli, ma terminazioni nervose che servono per sondare l’ambiente e, combinati con il loro olfatto finissimo, riescono a esacerbare l’identificazione di qualsiasi odore.",
        "Dopo aver mangiato i gatti si lavano immediatamente: si tratta di un istinto primordiale di sopravvivenza che li porta a nascondere l’odore di cibo dai predatori per non essere attaccati.",
        "I gatti hanno cinque artigli sulle zampe anteriori, ma solo quattro su quelle posteriori.",
        "I gatti detestano l’odore di cipolla e di aceto.",
        "La lingua dei gatti è composta da piccoli “ganci”, che servono sia a lacerare il cibo che a lavarsi.",
        "La dieta ideale di un gatto dovrebbe contenere dei grassi, perché il loro corpo non ne produce.",
        "Convenzionalmente si crede che i gatti non siano in grado di distinguere i colori. Recentemente è stato invece dimostrato che sanno vedere perfettamente il blu, il verde e il rosso.",
        "Il gatto apparve sulla Terra prima del cane e di molti animali diventati da compagnia, ma fu uno degli ultimi ad essere addomesticati.",
        "Quando un gatto fa le fusa non significa necessariamente che sia rilassato. Il gatto emette lo stesso identico suono quando è spaventato per rassicurarsi.",
        "I gatti possono emettere un centinaio di suoni differenti (i cani si fermano a dieci). Ogni gatto ha i suoi personalissimi “miao” e “purr”, che sono sempre diversi da individuo a individuo.",
        "La vita media di un gatto varia tra i 12 e i 15 anni. Raggiunge la maturità intorno ai 5 anni e la terza età intorno ai 10."
    ]
    listfotogatti = ["http://i0.kym-cdn.com/photos/images/original/000/191/654/Longcat_buildings.jpg",
                     "http://vignette4.wikia.nocookie.net/uncyclopedia/images/f/ff/Longcat_War.jpg",
                     "http://vignette2.wikia.nocookie.net/uncyclopedia/images/2/24/There_can_only_be_one_Longcat.jpg",
                     "http://www.catster.com/wp-content/uploads/2015/06/600px-outer-space-longcat-6ztyxR.jpg",
                     "http://blog.seanbonner.com/wp-content/uploads/2009/07/1246818283203.jpg",
                     "https://caterville.files.wordpress.com/2013/11/40c39-longcat2.jpg",
                     "http://i2.kym-cdn.com/photos/images/original/000/009/947/longcat_ark_by_skunk419.jpg",
                     "http://i0.kym-cdn.com/photos/images/newsfeed/000/009/709/750pxtacgnolahk2.jpg",
                     "http://i2.kym-cdn.com/photos/images/newsfeed/000/002/115/longcat-rampage.jpg",
                     "http://i2.kym-cdn.com/photos/images/original/000/600/858/45e.jpg",
                     "http://i1.kym-cdn.com/photos/images/original/000/003/402/4chan-1206886720300.jpg"]
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=random.choice(listgatti))
    bot.send_photo(chat_id=chat_id, photo=random.choice(listfotogatti))


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
    dp.add_handler((CommandHandler("quokkas", quokka)))
    dp.add_handler((CommandHandler("schlingel", gatti)))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
