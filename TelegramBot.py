import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

bot = telebot.TeleBot('1935772262:AAHaap-tlxJxOsDzzI85c0ApfP4_8hmzDVw')

keyboard = types.ReplyKeyboardMarkup(row_width = 4)

button1 = types.KeyboardButton('USD-UAH')
button2 = types.KeyboardButton('EUR-UAH')
button3 = types.KeyboardButton('RUB-UAH')
button4 = types.KeyboardButton('UAH-USD')
button5 = types.KeyboardButton('USD-EUR')
button6 = types.KeyboardButton('EUR-USD')
button7 = types.KeyboardButton('RUB-USD')
button8 = types.KeyboardButton('UAH-EUR')
button9 = types.KeyboardButton('USD-RUB')
button10 = types.KeyboardButton('EUR-RUB')
button11 = types.KeyboardButton('RUB-EUR')
button12 = types.KeyboardButton('UAH-RUB')

keyboard.add(button1, button2, button3, button4, button5,
             button6, button7, button8, button9, button10,
             button11, button12)


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите интересующий вас курс валюты:', reply_markup = keyboard)
@bot.message_handler(content_types = ['text'])
def handler(message):
    if message.text == 'USD-UAH':
        dollar_grn = 'https://finance.rambler.ru/calculators/converter/1-USD-UAH/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(dollar_grn, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс доллара к гривне - ' + teg[0].text)
    elif message.text == 'USD-EUR':
        dollar_euro = 'https://finance.rambler.ru/calculators/converter/1-USD-EUR/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(dollar_euro, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс доллара к евро - ' + teg[0].text)
    elif message.text == 'USD-RUB':
        dollar_rub = 'https://finance.rambler.ru/calculators/converter/1-USD-RUB/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(dollar_rub, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс доллара к рублю - ' + teg[0].text)
    elif message.text == 'EUR-UAH':
        euro_grn = 'https://finance.rambler.ru/calculators/converter/1-EUR-UAH/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(euro_grn, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс евро к гривне - ' + teg[0].text)
    elif message.text == 'EUR-USD':
        euro_dollar = 'https://finance.rambler.ru/calculators/converter/1-EUR-USD/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(euro_dollar, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс евро к доллару - ' + teg[0].text)
    elif message.text == 'EUR-RUB':
        euro_rub = 'https://finance.rambler.ru/calculators/converter/1-EUR-RUB/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(euro_rub, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс евро к рублю - ' + teg[0].text)
    elif message.text == 'RUB-UAH':
        rub_grn = 'https://finance.rambler.ru/calculators/converter/1-RUB-UAH/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(rub_grn, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс рубля к гривне - ' + teg[0].text)
    elif message.text == 'RUB-USD':
        rub_dollar = 'https://finance.rambler.ru/calculators/converter/1-RUB-USD/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(rub_dollar, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс рубля к доллару - ' + teg[0].text)
    elif message.text == 'RUB-EUR':
        rub_euro = 'https://finance.rambler.ru/calculators/converter/1-RUB-EUR/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(rub_euro, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс рубля к евро - ' + teg[0].text)
    elif message.text == 'UAH-USD':
        grn_dollar = 'https://finance.rambler.ru/calculators/converter/1-UAH-USD/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(grn_dollar, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс гривны к доллару - ' + teg[0].text)
    elif message.text == 'UAH-EUR':
        grn_euro = 'https://finance.rambler.ru/calculators/converter/1-UAH-EUR/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(grn_euro, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс гривны к евро - ' + teg[0].text)
    elif message.text == 'UAH-RUB':
        grn_rub = 'https://finance.rambler.ru/calculators/converter/1-UAH-RUB/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

        page = requests.get(grn_rub, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        teg = soup.findAll('div', {'class': 'converter-display__cross-block'})
        bot.send_message(message.chat.id, 'Сейчас курс гривны к рублю - ' + teg[0].text)
    elif message.text == '/Info':
        bot.send_message(message.chat.id, 'Этот бот работает с 4 валютами : Доллар, Евро, Гривна, Рубль\n'
                                            '\n'
                                            'Что б узнать курс интересующей вас валюты выберите соответствующую кнопку, или введите её название. Для просмотра курса одной валюты к другой ведите между ними "-", или нажмите на определенную кнопку.\n'
                                            '(Например : USD-RUB)\n'
                                            '\n'
                                            'Что бы запустить программу - /start!')
    else:
        bot.send_message(message.chat.id, 'Напишите правильный курс или введите команду /Info')

bot.polling(none_stop = True, interval = 0)

