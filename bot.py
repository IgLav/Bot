import telebot
from telebot import types
from . import config
bot = telebot.TeleBot(config.TOKEN)
markup = types.ReplyKeyboardMarkup()
item1 = types.KeyboardButton('lol')
item2 = types.KeyboardButton('lal')
markup.row(item1, item2)



@bot.message_handler(commands=['start'])
def welcome(message):
     bot.reply_to(message, 'Привет', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def repeat(message):
     keyboard = types.InlineKeyboardMarkup()
     callback_button = types.InlineKeyboardButton(text='push', callback_data='lol')
     keyboard.add(callback_button)
     bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
