import telebot
from Config1 import keys, TOCEN

bot = telebot.TeleBot(TOCEN)

from Utils1 import ConvertionExeption, CriptoConverter

@bot.message_handler(commands=["text", "help", "start"])
def send_help(message:telebot.types.Message):
    text = "Чтобы начать работу введите команду Боту в следующем формате \n <Имя валюты>  \
<В какую валюту перевести> \
<Количество переводимой валюты> \ <Увидеть список всех доступных валют можно с помощью команды: /values>"
    bot.reply_to(message, text)

@bot.message_handler(commands=["values", ])
def values(message:telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types = ['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Неверное количество параметров')
        quote, base, amount = values
        total_base = CriptoConverter.convert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'

        bot.reply_to(message, text)

bot.polling(none_stop=True)