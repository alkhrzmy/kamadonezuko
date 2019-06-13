#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Kamado nezuko-chan bot
Sample bot t.me/kamadobot

'''
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from time import time

my_id = "694351915"
bot = telegram.Bot(token="844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30")


print("### Running ###")
print("_+ Username: " + bot.get_me()['username'])
bot.send_message(my_id, '[Notify] Bot Running\nt.me/kamadobot')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
  update.message.reply_text('Started!')

def help(update, context):
  update.message.reply_text('Soon!')
  
def echo(update, context):
  update.message.reply_text(update.message.text)
  
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
  










if __name__ == '__main__':
    main()
