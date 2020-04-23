import json

import telebot
#import config
#import pb
from _datetime import datetime
import array


bot = telebot.TeleBot('1130369334:AAFgLffnH_KriPTGWEN4nMKgSm3qighfXJU')

posts = []

class PostClass:
    def __init__(self, id, post, time):
        self.id = id
        self.post = post
        self.time = time

    def str(self):
        return '{}, {}'.format(self.post, self.time)

time = datetime.now()
post = ''
id=0


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Creator', callback_data='get-Creator')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Editor', callback_data='edit-Editor')
    )

    bot.send_message(message.chat.id, 'Hi! Choose who are you today', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_callback(query)
    elif data.startswith('edit-'):
        get_callback_edit(query)
    elif data.startswith('do-'):
        get_callback_do(query)
    elif data.startswith('send-'):
        get_callback_send(query)
    elif data.startswith('see-'):
        get_callback_see(query)
    elif data.startswith('ent-'):
        get_callback_ent(query)
    elif data.startswith('rep-'):
        get_callback_rep(query)

def get_callback(query):
    bot.answer_callback_query(query.id)
    send_result(query.message)

def get_callback_edit(query):
    bot.answer_callback_query(query.id)
    send_result_edit(query.message)

def send_result(message):
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Make Post', callback_data='do-Make Post')
        #telebot.types.InlineKeyboardButton('Send Content for Moderation', callback_data='send-Send Content for Moderation'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('See Orders', callback_data='see-See Orders'),
    )
    bot.send_message(
        message.chat.id, 'What do you want to do?',
        reply_markup=keyboard
    )

def send_result_edit(message):
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Enter The Order Number', callback_data='ent-Enter The Order Number')
    )
    bot.send_message(
        message.chat.id, 'My Orders',
        reply_markup=keyboard
    )

def get_callback_ent(query):
    bot.answer_callback_query(query.id)
    send_result_ent(query.message)

def send_result_ent(message):
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Reply With The Completed Work',
                                           callback_data='rep-Reply With The Completed Work')
    )
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.isdigit() :
            bot.send_message(
                message.chat.id, 'My Orders',
                reply_markup=keyboard
                )
        else:
            bot.send_message(
                message.chat.id, 'Please enter the number'
            )

def get_callback_rep(query):
    bot.answer_callback_query(query.id)
    send_result_rep(query.message)

def send_result_rep(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id, 'Completed Work Sent Back'
    )

def get_callback_do(query):
    bot.answer_callback_query(query.id)
    send_result_to_do(query.message)

def send_result_to_do(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'Write your post')
    bot.register_next_step_handler(message, write_post)

def write_post(message):
    post = message.text
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Send Content for Moderation',
                                           callback_data='send-Send Content for Moderation'),
    )
    bot.send_message(message.chat.id, 'Choose Date When You Want To Post')

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.isdigit():
            bot.send_message(
                message.chat.id, 'My Orders',
                reply_markup=keyboard
            )
        else:
            bot.send_message(
                message.chat.id, 'Please enter the number'
            )
    p = PostClass(id, post, time)
    posts.append(p)




def get_callback_send(query):
    bot.answer_callback_query(query.id)
    send_result_to_send(query.message)

def send_result_to_send(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id, 'Content Sent'
    )



def get_callback_see(query):
    bot.answer_callback_query(query.id)
    send_result_to_see(query.message)


def send_result_to_see(message):
    bot.send_chat_action(message.chat.id, 'typing')
    p = [post.str() for post in posts]
    bot.send_message(
        message.chat.id, 'Orders: ', p
    )


bot.polling(none_stop=True)

#keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
#keyboard1.row('Creator', 'Editor')

#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'Hi. Choose who are you today', reply_markup=keyboard1)
