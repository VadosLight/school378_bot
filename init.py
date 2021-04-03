import telebot
import requests
import config
import logging

# Warning: Do not send more than about 4000 characters each message, otherwise you'll risk an HTTP 414 error.

# инициализируем бота
bot = telebot.TeleBot(config.token)

# пишем полные логи в консоль
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

# response = requests.get('https://api.github.com')
# print(response.status_code)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print("Бот увидел сообщение " + message.text)
    bot.send_message(message.chat.id, message.text)


@bot.channel_post_handler(content_types=["text"])
def hi(message):
    bot.send_message(config.channel_id, message.text)
    # print("Бот увидел пост в канале ", message.chat.id)


if __name__ == '__main__':
    bot.infinity_polling()
