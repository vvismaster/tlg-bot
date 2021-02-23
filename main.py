import socket
import telebot

bot = telebot.TeleBot('1296185221:AAEbNrkE3ZMjqGemdp710UOXBwQzThbvKNo')

hostname = socket.gethostname()

keyboardNodes = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardElection = telebot.types.ReplyKeyboardMarkup(True, True)

keyboardNodes.row('TimeDiff','cpu', 'net', 'DePoolBalance', 'WalletBalance', 'TickTock', 'DePoolRequest')
keyboardElection.row('State','StartEnd')

@bot.message_handler(commands=['node'])
def send_text(message):
    bot.send_message(message.chat.id, 'Command', reply_markup=keyboardNodes)

@bot.message_handler(commands=['election'])
def send_text(message):
    bot.send_message(message.chat.id, 'Command', reply_markup=keyboardElection)

bot.polling()