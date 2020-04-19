import json

import telebot
import config
#import pb

bot = telebot.TeleBot('1130369334:AAFgLffnH_KriPTGWEN4nMKgSm3qighfXJU')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Creator', callback_data='get-Creator')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Editor', callback_data='get-Editor')
    )

    bot.send_message(message.chat.id, 'Hi! Choose who are you today', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_callback(query)
    elif data.startswith('do-'):
        get_callback_do(query)
    elif data.startswith('send-'):
        get_callback_send(query)
    elif data.startswith('create-'):
        get_callback_create(query)
    elif data.startswith('see-'):
        get_callback_see(query)

def get_callback(query):
    bot.answer_callback_query(query.id)
    send_result(query.message)

def send_result(message):
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Make Post', callback_data='do-Make Post'),
        telebot.types.InlineKeyboardButton('Send Content for Moderation', callback_data='send-Send Content for Moderation'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Create a Custom Post', callback_data='create-Create a Custom Post'),
        telebot.types.InlineKeyboardButton('See Orders', callback_data='see-See Orders'),
    )
    bot.send_message(
        message.chat.id, 'What do you want to do?',
        reply_markup=keyboard
    )


def get_callback_do(query):
    bot.answer_callback_query(query.id)
    send_result_to_do(query.message)

def send_result_to_do(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id, 'Post Created'
    )

def get_callback_send(query):
    bot.answer_callback_query(query.id)
    send_result_to_send(query.message)

def send_result_to_send(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id, 'Content Sent'
    )

def get_callback_create(query):
    bot.answer_callback_query(query.id)
    send_result_to_create(query.message)


def send_result_to_create(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id, 'Custom Post Created'
    )

def get_callback_see(query):
    bot.answer_callback_query(query.id)
    send_result_to_see(query.message)


def send_result_to_see(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id, 'Orders: '
    )


bot.polling(none_stop=True)

#keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
#keyboard1.row('Creator', 'Editor')

#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'Hi. Choose who are you today', reply_markup=keyboard1)