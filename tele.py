# -*- coding: utf-8 -*-

'''

Kamado nezuko-chan bot
Sample bot t.me/kamadobot

'''
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telebot import types
from time import time

my_id = "694351915"
bot = telebot.Bot(token="844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30")

print("### Running ###")
print("_+ Username: " + bot.get_me()['username'])
bot.send_message(my_id, 'Login bot sukses\nt.me/kamadobot')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)













if __name__ == '__main__':
    main()
