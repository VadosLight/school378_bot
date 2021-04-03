import telebot
import config
import sys

# инициализируем бота
bot = telebot.TeleBot(config.token)

def sendMessage(msg):
    bot.send_message(config.channel_id, msg)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sendMessage(sys.argv[1])
