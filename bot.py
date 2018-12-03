import os
import time
import telebot
from random import randint
from flask import Flask, request

token = "736499313:AAEkYrlxvxRYQW2WppS-xXdeZpznM5KGTSY"

bot = telebot.TeleBot(token)
names = "murmuring-savannah-17399"
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    text_of_message = 'Вас приветсвует бот канала @Unilecs! 🖥 Чем я могу вам помочь?🔖'
    bot.send_message(message.from_user.id, text_of_message)

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Hello", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(names, token))
    return "Hi", 200


if __name__ == "__main__":
    server.debug = True
    server.run()