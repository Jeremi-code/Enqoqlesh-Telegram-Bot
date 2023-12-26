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
    # Create a new markup for the message
    markup = types.ReplyKeyboardMarkup()
    key1= types.KeyboardButton('play With Friends')
    key2= types.KeyboardButton('help')
    markup.add(key1, key2)

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

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'play With Friends':
        if message.chat.type == 'private':
            bot.send_message(message.chat.id, 'You have to add the bot to a group and type /play')
        else:
            markup = types.ReplyKeyboardMarkup()
            genere1= types.KeyboardButton('All')
            genere2= types.KeyboardButton('History')
            genere3= types.KeyboardButton('Geography')
            genere4= types.KeyboardButton('Movie')
            genere5= types.KeyboardButton('Literature')
            genere6= types.KeyboardButton('Society')
            genere7= types.KeyboardButton('Science')

            markup.add(genere1, genere2, genere3, genere4, genere5, genere6, genere7)
            bot.send_message(message.chat.id, 'Choose a genere', reply_markup=markup)
            
            
            bot.send_message(message.chat.id, 'Processing play...')  
    elif message.text == 'help':
        bot.send_message(message.chat.id, 'Help message')  
    else:
        bot.reply_to(message, 'You said: ' + message.text)
bot.polling()
