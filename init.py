import telebot
import requests
import config
import logging

# response = requests.get('https://api.github.com')
# print(response.status_code)

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    bot.polling(none_stop=True)
