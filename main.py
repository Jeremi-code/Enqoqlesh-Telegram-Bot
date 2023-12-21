import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Create a new bot instance
bot = telebot.TeleBot(TOKEN)

# Handle the /start command


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Play')
    itembtn2 = types.KeyboardButton('Help')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Welcome to Nodemon", reply_markup=markup)

    # keyboard = types.InlineKeyboardMarkup(row_width=2)
    # play_button = types.InlineKeyboardButton(text='Play', callback_data='play')
    # help_button = types.InlineKeyboardButton(text='Help', callback_data='help')
    # keyboard.add(play_button, help_button)
    
    bot.send_message(message.chat.id, 'Welcome to Nodemon', reply_markup=markup)
# Handle all other messages
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'play':
        bot.send_message(call.message.chat.id, 'play with friends')
    elif call.data == 'help':
        bot.send_message(call.message.chat.id, 'help')

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, 'This is a nodemon .')


@bot.message_handler(commands=['stop'])
def handle_ranking(message):
    bot.reply_to(message, 'This is the stop message.')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'You said: ' + message.text)

# @bot.callback_query_handler(func=lambda call: True)
# def handle_button_click(call):
#     if call.data == 'play':
#         bot.send_message(call.message.chat.id, 'play with friends')
#     elif call.data == 'help':
#         bot.send_message(call.message.chat.id, 'help')
# print("Bot is running...")

# Start the bot
bot.polling()
