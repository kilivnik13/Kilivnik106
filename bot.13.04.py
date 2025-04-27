import telebot
import requests
import random
from telebot import types

BOT_TOKEN = "7294844664:AAGqzZiJ3pKN5ghSYUOMPGACcdX1Mz0AD6A"
bot = telebot.TeleBot(BOT_TOKEN)

WEATHER_API_KEY = "bd6e0267940684a51406d6dfc5d46c1b"
CITY = "Moscow"

sticker_ids = [
    "CAACAgIAAxkBAAEOSXZn-iHIBmjo64zvjwFsCPrBgfecVgACKUYAApMqOEi1syNCkZsuPTYE",
    "CAACAgIAAxkBAAEOSXhn-iHgX5ITF7TTl7oYTiQeIajxWAACAwMAAqKK8QdEnxqHkjwAASc2BA",
    "CAACAgIAAxkBAAEOSXpn-iIaKR5y5OrsJZTod93INZESMQACQCIAAnq2YEur-eo2cza__jYE",
    "CAACAgIAAxkBAAEOSXxn-iJgDnxAniga0ogZJw1H5lq7dgAC0BYAAiFLYUsbw6MJkqkryzYE",
    "CAACAgIAAxkBAAEOSYBn-iJ8_1y4NPtVOYZmtbnaOMt0kwACoRoAAjNr8UlRn7snL37A0jYE",
    "CAACAgIAAxkBAAEOSYJn-iKUMSEC0pbAPgsVvJ_y_bkAAcIAAiswAAJycHBJ8cqoSpvaIy42BA",
    "CAACAgIAAxkBAAEOSaRn-iUNQC2Eao3_hnpt6HgWoqjFeQACHRwAAmGSQUsjVew9WLD5kTYE",
    "CAACAgQAAxkBAAEOSaxn-iVuj_OHjd436Sbg8FhbfeCJewACtQoAAgPw-FNs5Z3AzAP3_zYE",
]
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except (KeyError, TypeError):
        return None, "Ошибка получения данных о погоде"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather_button = types.KeyboardButton("Текущая погода")
    #markup.add(weather_button)
    sticker_button = types.KeyboardButton("Стикер")
    markup.add(weather_button, sticker_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать погоду или получить стикер.", reply_markup=markup)
    #bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать погоду.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def hello(message):
    bot.reply_to(message, "Привет, человек")

@bot.message_handler(func=lambda message: message.text == "Текущая погода")
def weather(message):
    temperature, description = get_weather(CITY)
    if temperature is not None:
        bot.send_message(message.chat.id, f"Погода в городе {CITY}: {temperature:.1f}°C, {description}")
    else:
        bot.send_message(message.chat.id, description)

@bot.message_handler(func=lambda message: message.text == "Стикер")
def sticker(message):
    random_sticker = random.choice(sticker_ids)
    bot.send_sticker(message.chat.id, random_sticker)


bot.infinity_polling()
