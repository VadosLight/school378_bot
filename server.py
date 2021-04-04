from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
import logging
import json


def sendMessage(msg, token, channel_id):
    bot = telebot.TeleBot(token)
    bot.send_message(channel_id, msg)
    # bot = telebot.TeleBot(config.token)
    # bot.send_message(config.channel_id, msg)

def getToken_botId_from_postData(post_data):
    json_data = post_data.decode('utf-8').replace('\\"', "")
    json_data = json_data.split(",")

    bot_id = json_data[len(json_data)-1].replace('}"', "").split(":")
    bot_id = bot_id[1].replace(" ", "")
    token = json_data[len(json_data)-2].split(":")
    token = f'{token[1]}:{token[2]}'.replace(" ", "")
    print(f"\n\n Токен = {token}\n Id бота = {bot_id}")
    return token, bot_id


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n",
                     str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(
            self.path).encode('utf-8'))

    def do_POST(self):
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)
        token, bot_id = getToken_botId_from_postData(post_data)

        decoded_data = post_data.decode('utf-8').replace('\\"', "").replace(',', '\n')
        # Убираем токен и айди бота
        decoded_data = decoded_data.replace(token, "***").replace(bot_id, "***") 
        logging.info(" data is: %s", decoded_data)

        sendMessage(decoded_data, token, bot_id)

        self._set_response()
        # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8000):
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
