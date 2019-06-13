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
bot = telegram.Bot(token="844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30")


print("### Running ###")
print("_+ Username: " + bot.get_me()['username'])
bot.send_message(my_id, 'Login bot sukses\nt.me/kamadobot')

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
  updater = Updater("844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30", use_context=True)
  dp = updater.dispatcher
  
  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help))
  
  # on noncommand i.e message - echo the message on Telegram
  dp.add_handler(MessageHandler(Filters.text, echo))

  # log all errors
  dp.add_error_handler(error)

  # Start the Bot
  updater.start_polling()
  
  # start_polling() is non-blocking and will stop the bot gracefully.
  updater.idle()











if __name__ == '__main__':
    main()
