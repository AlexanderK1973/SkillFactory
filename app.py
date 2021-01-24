import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    text_1 = f"Привет, {message.chat.first_name} {message.chat.last_name}!"
    text = 'Правила пользования:\n' \
           '- Чтобы увидеть весь перечень валют, введи команду\n/currency\n' \
           '- Для конвертации введи через пробел в одну строку:\n' \
           'название валюты,\n' \
           'в какую валюту перевести,\n' \
           'количество валюты для обмена.'
    bot.reply_to(message, text_1 + '\n' + text)


@bot.message_handler(commands=['currency'])
def values(message: telebot.types.Message):
    text = 'Перечень валют для обмена: '
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Не три параметра')

        quote, base, amount = map(str.lower, values)
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base * float(amount)}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
