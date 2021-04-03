import os
import sys
import requests
import json


class Args:
    def __init__(self, token, chatId):
        self.token = token
        self.chatId = chatId

    def isCorrectArgs(self):
        # 45 - примерная длина токена
        if(len(self.token) < 45):
            return False
        # 10 - примерная длина айди чата
        if(int(self.chatId) >= 0 or len(self.chatId) < 10):
            return False
        return True


class DataCollector:
    @staticmethod
    def diskCapacity():
        return 0


# Принимаем токен (строка) и id-бота (отрицательное число)
# sys.argv[1] и sys.argv[2]
# sys.argv[0] - это название файла
# адрес сервера встроить в код или принимать аргументом
if __name__ == "__main__":
    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    requests.post('http://188.134.69.199:8000', data=y)
    # if (len(sys.argv) == 3):
    #     args = Args(sys.argv[1], sys.argv[2])
    #     print(args.token, args.chatId)
    #     if(args.isCorrectArgs()):
    #         print("it`s all right")
    #         # Теперь вызываем функцию сбора данных а затем отправки на сервер
    #         requests.post('188.134.69.199:8000', data = {'key':'value'})
    #     else:
    #         print("Incorrect arguments. Remember, TOKEN is first")
    # else:
    #     print("Incorrect number of arguments")
