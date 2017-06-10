import requests
import json
import time


URL = "https://api.telegram.org/bot322854984:AAG34-oiQAUW2tpu3JDtkSaUnHPzf8xhqO0/"

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

text, chat =   get_last_chat_id_and_text(get_updates())
if text == "come va":
    send_message("bene", chat)
if text == "suca":
    send_message("milla", chat)
else:
    send_message("non ho capito", chat)