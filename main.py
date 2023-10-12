import telebot
from telebot import types

# Имя бота @victor345_bot
token = '6368536776:AAHnKMcThWAz4wrEBCLGblPPAhq1moXk7GI'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("Пока")
    btn3 = types.KeyboardButton("Предметы")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, text="Привеет...)")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, text="Поока...(")
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, "Меня зовут Victor")
    elif message.text == "Что ты умеешь?":
        bot.send_message(message.chat.id, text="Пока ничего(")
    elif message.text == "Предметы":
        button1 = types.KeyboardButton("История")
        button2 = types.KeyboardButton("Орг")
        markup.add(button1, button2)
    else:
        bot.send_message(message.chat.id, text="К сожалению, я тебя не понимаю")


bot.polling(none_stop=True)
