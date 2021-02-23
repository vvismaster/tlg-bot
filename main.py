import telebot

bot = telebot.TeleBot('1296185221:AAEbNrkE3ZMjqGemdp710UOXBwQzThbvKNo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()