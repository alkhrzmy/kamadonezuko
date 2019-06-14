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

  
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
  # global bot
  updater = Updater(token="844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30")
  disp = updater.dispatcher
  
  
  id_chat = bot.get_updates()[0]['message']['chat']['id']
  '''
  cmd = bot.get_updates()[0]
  if cmd == '/start':
    bot.send_message(id_chat, "Hi! This bot still in developing by creator, please don't use this bot")
  elif cmd == 'test':
    bot.send_message(id_chat, "masuk")
  else:
    disp.add_error_handler(error)
  '''
  disp.add_handler(CommmandHandler("start", bot.sendMessage(id_chat, 'Hi!')
  updater.start_polling()
  updater.idle()









if __name__ == '__main__':
    main()
