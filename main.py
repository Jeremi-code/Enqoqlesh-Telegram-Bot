import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Create a new bot instance
bot = telebot.TeleBot(TOKEN)

# Handle the /start command


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Hello! I am your Telegram bot.')

# Handle all other messages


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, 'This is a help message.')


@bot.message_handler(commands=['stop'])
def handle_ranking(message):
    bot.reply_to(message, 'This is the stop message.')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'You said: ' + message.text)


print("Bot is running...")

# Start the bot
bot.polling()
