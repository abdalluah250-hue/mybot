import os
import telebot

# يسحب التوكن من Railway تلقائياً
TOKEN = os.getenv('TELE_...') 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "تم الربط! البوت يعمل الآن من خلال Railway.")

bot.polling()
