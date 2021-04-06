from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
import logging
import json


def sendMessage(msg, token, channel_id):
    bot = telebot.TeleBot(token)
    bot.send_message(channel_id, msg)
    # bot = telebot.TeleBot(config.token)
    # bot.send_message(config.channel_id, msg)


def decodedDataToMessage(data):
    jsonData = json.dumps(data)
    jsonData = jsonData[1:-1].replace(",", "\n\n").replace(";", "\n")

    markupDict = {'<celsius>': '°'}

    for key, val in markupDict.items():
        jsonData = jsonData.replace(key, val)

    # print(jsonData)
    return jsonData.replace('"', '')


class Server(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        # Получает размер данных и сами данные
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Преобразуем поломанный JSON в словарь
        decoded_data = post_data.decode('utf-8').replace('\\', "")
        decoded_data = json.loads(decoded_data[1:-1])

        # Убираем токен и айди бота из данных, записываем их в переменные
        token = decoded_data.pop("token")
        bot_id = decoded_data.pop("bot_id")

        # Пишем логи
        # logging.info('Data is:\n{decoded_data}')

        decodedDataToMessage(decoded_data)
        sendMessage(decodedDataToMessage(decoded_data), token, bot_id)

        self._set_response()
        # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)

    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    portInput = int(input("Type the PORT: "))
    if(portInput > 10 and portInput < 10000):
        run(port=portInput)
