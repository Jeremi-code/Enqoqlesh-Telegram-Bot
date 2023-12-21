import telebot

# Create a new bot instance
bot = telebot.TeleBot('6860778430:AAGFxWzKy5nPhmarJwLNu9KM-BWsl4Z79OU')

# Handle the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Hello! I am your Telegram bot.')

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'You said: ' + message.text)

# Start the bot
bot.polling()
