import os
import sys
import requests
import json

import getpass
import socket
import psutil
import platform
from datetime import datetime
from uuid import getnode as get_mac
from speedtest import Speedtest
inet = Speedtest()


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

    def __init__(self):
        self.name = getpass.getuser()
        self.ip = socket.gethostbyname(socket.getfqdn())
        self.mac = get_mac()
        self.ost = self.osInfo()
        self.cpu = psutil.cpu_freq()
        # self.download_MB_S = float(str(inet.download())[0:2] + "."  # Входящая скорость
        #                       + str(round(inet.download(), 2))[1]) * 0.125
        # self.uploads_MB_S = float(str(inet.upload())[0:2] + "."   # Исходящая скорость
        #                      + str(round(inet.download(), 2))[1]) * 0.125
        self.disc_usage = self.diskCapacity()

    @staticmethod
    def osInfo():
        ost = platform.uname()
        return f'OS={ost.system}_{ost.release}_{ost.machine}'

    @staticmethod
    def diskCapacity():
        disk_C = psutil.disk_usage("C:/")
        disk_C_total_GB = round(disk_C[0]/1024/1024/1024)
        disk_C_free_GB = round(disk_C[2]/1024/1024/1024)
        disk_C_percent = disk_C[3]
        info_C = f'Toltal_Memory: {disk_C_total_GB} GB, Free_Memory: {disk_C_free_GB} GB, Usage_%: {disk_C_percent}'
        return info_C


# Принимаем токен (строка) и id-бота (отрицательное число)
# sys.argv[1] и sys.argv[2]
# sys.argv[0] - это название файла
# адрес сервера встроить в код или принимать аргументом
if __name__ == "__main__":
    if (len(sys.argv) == 3):
        args = Args(sys.argv[1], sys.argv[2])
        print(args.token, args.chatId)
        if(args.isCorrectArgs()):
            print("it`s all right")
            # Теперь вызываем функцию сбора данных а затем отправки на сервер
            obj = DataCollector()
            obj.token = sys.argv[1]
            obj.bot_id = sys.argv[2]
            x = json.dumps(obj.__dict__)
            # Принимать ещё одним аргуменотм?
            requests.post('http://188.134.69.199:8000', json=x)
        else:
            print("Incorrect arguments. Remember, TOKEN is first")
    else:
        print("Incorrect number of arguments")
