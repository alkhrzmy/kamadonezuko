# -*- coding: utf-8 -*-

'''

Kamado nezuko-chan bot
Sample bot t.me/kamadobot

'''
import telepot
import time
from humanfriendly import format_timespan, format_size, format_number, format_length
from telepot.loop import MessageLoop
programStart = time.time()

token = "844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30"
bot = telepot.Bot(token)
my_id = '694351915'

def handle(self):
        # print(self)
        content_type, chat_type, chat_id= telepot.glance(self)

        print("_+ Message arrived: " + self['text'])
        command = self['text'].strip().lower()
        if command ==  '/start':
          bot.sendMessage(chat_id, "Hi! thanks for your message. This bot still in developing mode", reply_to_message_id=self['message_id'])
        elif command == '/speed':
          startTime = time.time()
          bot.sendMessage(chat_id, 'Counting bot speed...')
          elapseTime = time.time() - startTime
          bot.sendMessage(chat_id, 'Speed sending message took %f second' % elapseTime)
        elif command == '/check':
                startTime = time.time()
                bot.sendMessage(chat_id, 'Please wait...')
                elapseTime = time.time() - startTime
                timeRunning = time.time() - programStart
                bot.sendMessage(chat_id, 'Bot already running '+format_timespan(timeRunning)+'\nBot response speed is %0.3f seconds\nBot is using Heroku Python 3.6.8' % elapseTime)
        else:
          bot.sendMessage(chat_id, "Hi! thanks for your message. Your message is " + self['text'])

MessageLoop(bot, handle).run_as_thread()
print ('Running...')

# Keep the program running.
while 1:
    time.sleep(1)
