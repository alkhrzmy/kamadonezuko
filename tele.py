# -*- coding: utf-8 -*-

'''

Kamado nezuko-chan bot
Sample bot t.me/kamadobot

'''
import telepot
import time
from telepot.loop import MessageLoop

token = "844244943:AAGzMVzum7nTCrqLDr50Vccpu_ieco3RC30"
bot = telepot.Bot(token)
my_id = '694351915'

def handle(self):
        # print(self)
        content_type, chat_type, chat_id = telepot.glance(self)

        print("_+ Message arrived: " + self['text'])
        command = self['text'].strip().lower()
        if command ==  '/start':
          bot.sendMessage(chat_id, "Hi! thanks for your message. This bot still in developing mode")
        elif command == '/speed':
                startTime = time.time()
                elapseTime = time.time() - startTime
                bot.sendMessage(chat_id, 'Bot speed took %f second' % elapseTime)
        elif command.startswith('https://t.me/'):
                bot.sendMessage(chat_id, command[12:])
        else:
          bot.sendMessage(chat_id, "Hi! thanks for your message. Your message is " + self['text'])
        

MessageLoop(bot, handle).run_as_thread()
print ('Running...')

# Keep the program running.
while 1:
    time.sleep(1)
