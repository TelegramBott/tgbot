import telebot
from telebot import types
import csv


def update_csv(text, index, id):
    data, ids = [], []
    with open('da'
              'ta.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            data.append(row)
            if row[0] != 'id':
                ids.append(int(row[0]))
    if int(id) in ids:
        data[ids.index(int(id)) + 1][index] = text
    else:
        new = []
        for i in range(9):
            new.append('')
        new[0], new[index] = id, text
        data.append(new)
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in data:
            writer.writerow(i)

def check_hw(id):
    data, ids = [], []
    with open('data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            data.append(row)
            if row[0] != 'id':
                ids.append(int(row[0]))
    if int(id) in ids:
        return data[ids.index(int(id)) + 1]
    return 0


def set_matan(mes):
    update_csv(mes.text, 1, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_dis(mes):
    update_csv(mes.text, 2, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_log(mes):
    update_csv(mes.text, 3, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_eng(mes):
    update_csv(mes.text, 4, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_algem(mes):
    update_csv(mes.text, 5, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_hist(mes):
    update_csv(mes.text, 6, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_org(mes):
    update_csv(mes.text, 7, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


def set_prog(mes):
    update_csv(mes.text, 8, mes.from_user.id)
    bot.send_message(mes.chat.id, "Изменения внесены")


# Имя бота @victor345_bot
token = '6368536776:AAHnKMcThWAz4wrEBCLGblPPAhq1moXk7GI'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Д/З")
    btn2 = types.KeyboardButton("Расписание")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Д/З":
        murkup1 = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton('Добавить Д/З', callback_data='addhw')
        b2 = types.InlineKeyboardButton('Посмотреть Д/З', callback_data='checkhw')
        murkup1.row(b1, b2)
        bot.send_message(message.chat.id, text="Выберете действие:", reply_markup=murkup1)
    elif message.text == "Расписание":
        img = open('raspisanieHiWeek.png', "rb")
        bot.send_photo(message.chat.id, img, caption='расписание')


@bot.callback_query_handler(func=lambda callback: True)

def callback_message(callback):
    if callback.data == 'addhw':
        murkup3 = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton('Мат. анализ', callback_data='addhwmatan')
        b2 = types.InlineKeyboardButton('МЛиДМ', callback_data='addhwdis')
        b3 = types.InlineKeyboardButton('ЛиТА', callback_data='addhwlog')
        b4 = types.InlineKeyboardButton('Англ. яз.', callback_data='addhweng')
        b5 = types.InlineKeyboardButton('АлГем', callback_data='addhwalgem')
        b6 = types.InlineKeyboardButton('История', callback_data='addhwhist')
        b7 = types.InlineKeyboardButton('ОРГ', callback_data='addhworg')
        b8 = types.InlineKeyboardButton('ОАиП', callback_data='addhwprog')
        murkup3.add(b1, b2, b3, b4, b5, b6, b7, b8)
        bot.send_message(callback.message.chat.id, 'Добавление домашки', reply_markup=murkup3)
    elif callback.data == 'checkhw':
        res = 'Ваше домашнее задание:\n'
        output = check_hw(callback.message.chat.id)
        print(callback.message.chat.id)
        if output:
            output = output[1:]
            if output[0]:
                res += f'Мат. анализ: {output[0]}\n'
            if output[1]:
                res += f'МЛИДМ: {output[1]}\n'
            if output[2]:
                res += f'ЛИТА: {output[2]}\n'
            if output[3]:
                res += f'Английский язык: {output[3]}\n'
            if output[4]:
                res += f'АиГ: {output[4]}\n'
            if output[5]:
                res += f'История: {output[5]}\n'
            if output[6]:
                res += f'ОРГ: {output[6]}\n'
            if output[7]:
                res += f'ОАИП: {output[7]}'

            bot.send_message(callback.message.chat.id, res)
        else:
            bot.send_message(callback.message.chat.id, 'У вас нет домашнего задания')
    elif callback.data == 'tod':
        bot.send_message(callback.message.chat.id, 'Расписание на сегодня')
    elif callback.data == 'tom':
        bot.send_message(callback.message.chat.id, 'Расписание на завтра')
    elif callback.data == 'wee':
        bot.send_message(callback.message.chat.id, 'Расписание на неделю')
    elif callback.data == 'addhwmatan':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по Мат. анализу")
        bot.register_next_step_handler(message, set_matan)
    elif callback.data == 'addhwdis':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по МЛДИМ")
        bot.register_next_step_handler(message, set_dis)
    elif callback.data == 'addhwlog':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по ЛИТе")
        bot.register_next_step_handler(message, set_log)
    elif callback.data == 'addhweng':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по Английскому языку")
        bot.register_next_step_handler(message, set_eng)
    elif callback.data == 'addhwalgem':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по Алгебре и геометрии")
        bot.register_next_step_handler(message, set_algem)
    elif callback.data == 'addhwhist':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по Истрии")
        bot.register_next_step_handler(message, set_hist)
    elif callback.data == 'addhworg':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по ОРГ")
        bot.register_next_step_handler(message, set_org)
    elif callback.data == 'addhwprog':
        message = bot.send_message(callback.message.chat.id, "Введите домашнее задание по ОАИП")
        bot.register_next_step_handler(message, set_prog)


bot.polling(none_stop=True)

