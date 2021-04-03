import os
import sys
import requests
import argparse


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


# Принимаем токен (строка) и id-бота (отрицательное число)
# sys.argv[1] и sys.argv[2]
# sys.argv[0] - это название файла
if __name__ == "__main__":
    if (len(sys.argv) == 3):
        args = Args(sys.argv[1], sys.argv[2])
        print(args.token, args.chatId)
        if(args.isCorrectArgs()):
            print("it`s all right")
            # Теперь вызываем функцию сбора данных а затем отправки на сервер
        else:
            print("Incorrect arguments. Remember, TOKEN is first")
    else:
        print("Incorrect number of arguments")
