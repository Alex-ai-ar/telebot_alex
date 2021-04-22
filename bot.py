import telebot

bot = telebot.TeleBot('1727477469:AAGBOXQLvI5CLnN4AdUtp5qNNtG05X2NKC0')

@bot.message_handler(commands = ['start','help'])
def welcome(message):
    bot.reply_to(message, 'Привет, я бот Джерри, повторяю твои фразы')

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()