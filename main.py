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
    bot.send_message(message.chat.id, "Welcome to Nodemon. Type /help for assistance.")

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
    
def handle_new_chat_members(message):
    chat_id = message.chat.id
    group_title = message.chat.title

    for new_member in message.new_chat_members:
        if new_member.id == bot.get_me().id:
            # The bot has been added to the group
            bot.reply_to(message, f'Thank you for adding me to {group_title}! If you have any questions, feel free to ask.')

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def handle_new_chat_members_wrapper(message):
    # Ignore if there are other new members in the group
    if bot.get_me() in message.new_chat_members:
        handle_new_chat_members(message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'You said: ' + message.text)

bot.polling()
