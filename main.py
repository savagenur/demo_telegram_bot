from imaplib import Commands
import telebot
from telebot import types

bot = telebot.TeleBot('5555135641:AAFhCd_SDq0W4GysmUKTMLW7NdKJtWOiRLo')
task = ''


@bot.message_handler(commands=['start'])
def start(message):
    # text = f'Привет, <b>{message.from_user.first_name} {message.from_user.first_name}</b>.'
    # bot.send_message(message.chat.id, text, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(row_width=1)
    task1 = types.KeyboardButton(
        'Задачи')
    task2 = types.KeyboardButton(
        "Топ по готовым")
    task3 = types.KeyboardButton("Сводка")
    task4 = types.KeyboardButton("Мои задачи")
    task5 = types.KeyboardButton("Свободные заявки")
    markup.add(task1, task2, task3, task4, task5)
    bot.send_message(message.chat.id, "Выберите команду, \nкоторая вас интересует:",
                     reply_markup=markup, )


@bot.message_handler(commands=['Задачи'])
def tasks(message):
    # text = f'Привет, <b>{message.from_user.first_name} {message.from_user.first_name}</b>.'
    # bot.send_message(message.chat.id, text, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(row_width=1)
    task1 = types.KeyboardButton(
        'Заявка на систему очищения канализации, с. Ленинское ул. Баатыра 32')
    task2 = types.KeyboardButton(
        'Заявка на прокладку труб, с. Сокулук, ул. Абая 89/2')
    task3 = types.KeyboardButton('Заявка на вывоз мусора, пр. Жибек Жолу 109')

    markup.add(task1, task2, task3)
    bot.send_message(message.chat.id, "Выберите задачу:",
                     reply_markup=markup, )


@bot.message_handler(commands=["Топ по готовым"])
def done(message):
    text = '<b>Топы по выполненным заявкам за - сегодня:</b>\nАзаматов Азамат 2\nБакыт Бакытов 2\nАзиз Азизов 1\nКирилл Кириллов 1'
    bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(commands=['Свободные заявки'])
def available_tasks(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Принять', callback_data='whatever')
    markup.add(button)
    bot.send_message(message.chat.id, 'Заявка на систему очищения канализации, с. Ленинское ул. Баатыра 32',
                     reply_markup=markup, )


@bot.message_handler(commands=['Сводка'])
def analytics(message):
    text = '''
Заявка на систему очищения канализации, с. Ленинское ул. Баатыра 32
<b>Принято Азаматом Азаматовым</b>
Заявка на прокладку труб, с. Сокулук, ул. Абая 89/2
<b>Принято Бла Бла Бла</b>
Заявка на вывоз мусора, пр. Жибек Жолу 109
<b>Принято Аскаром Аскаровым</b>
'''
    bot.send_message(message.chat.id, text, parse_mode='html')





@bot.message_handler(commands=['choose'])
def choose1(message):

    # returns an InlineKeyboardMarkup with two buttons in a row, one leading to Twitter, the other to facebook
    # and a back button below

    # kwargs can be:

    markup = telebot.util.quick_markup({
        'Изменить статус': {'callback_data': 'whatever'},
        'Отказаться': {'callback_data': 'whatever'}
    }, row_width=2)

    bot.send_message(message.chat.id, 'Заявка на систему очищения канализации, с. Ленинское ул. Баатыра 32',
                     reply_markup=markup, )


@bot.message_handler(commands=['Мои задачи'])
def my_tasks(message):
    choose1(message=message)
    choose1(message=message)
    choose1(message=message)
    bot.send_message(message.chat.id,'.',  parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе привет!)', parse_mode='html')
    # Tasks
    elif message.text == 'Заявка на систему очищения канализации, с. Ленинское ул. Баатыра 32':
        bot.send_message(
            message.chat.id, 'Заявка на систему очищения канализации, с. Ленинское ул. Баатыра 32\n<b>Заявка принята вами</b>', parse_mode='html')
        start(message=message)
    elif message.text == 'Заявка на прокладку труб, с. Сокулук, ул. Абая 89/2':
        bot.send_message(
            message.chat.id, 'Заявка на прокладку труб, с. Сокулук, ул. Абая 89/2\n<b>Заявка принята вами</b>', parse_mode='html')
        start(message=message)

    elif message.text == 'Заявка на вывоз мусора, пр. Жибек Жолу 109':
        bot.send_message(
            message.chat.id, 'Заявка на вывоз мусора, пр. Жибек Жолу 109\n<b>Заявка принята вами</b>', parse_mode='html')
        start(message=message)

    # Methods
    elif message.text == "Задачи":
        tasks(message=message)
    elif message.text == "Топ по готовым":
        done(message=message)
    elif message.text == "Сводка":
        analytics(message=message)
    elif message.text == 'Мои задачи':
        my_tasks(message=message)
    elif message.text == 'Свободные заявки':
        available_tasks(message=message)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю!")


bot.polling(none_stop=True)
