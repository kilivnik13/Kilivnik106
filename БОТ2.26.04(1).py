import telebot
from datetime import datetime
import random

BOT_TOKEN = "7547845922:AAE3j6MFe-ASbJSRprcQbHkyAAnQu4-kf5Y"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    time_button = types.KeyboardButton("ПЖ time")
    number_button = types.KeyboardButton("Рандом")
    id_button = types.KeyboardButton("IDшeчка")
    markup.add(time_button,number_button, id_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать время, число от 1 до 100 или получить ид.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'ПЖ time':
        current_time = datetime.now().strftime('%H:%M:%S')
        bot.send_message(message.chat.id, f"Текущее время: {current_time}")
    elif message.text == 'Рандом':
        rand_num = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Случайное число: {rand_num}")
    elif message.text == 'IDшeчка':
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
    else:
        bot.send_message(message.chat.id, "Команда не распознана.")
        
print("Всё готово!")
bot.polling()
