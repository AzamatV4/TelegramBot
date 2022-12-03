import telebot

bot = telebot.TeleBot('5882973781:AAGyGgJNzSWnZukjLgieavTP8tqQAjBUguk')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'работает')

@bot.message_handler(commands=['claim'])
def claim(message):
    bot.send_message(message.chat.id, 'code')

bot.polling(none_stop=True)