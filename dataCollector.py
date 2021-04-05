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

# Знак ";" служит как символ новой строки.


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
        self.ip = socket.gethostbyname(socket.getfqdn())
        self.name = getpass.getuser()
        self.mac = self.getMac()
        self.ost = self.osInfo()
        self.cpu = self.cpuInfo()
        # self.download_MB_S = float(str(inet.download())[0:2] + "."  # Входящая скорость
        #                       + str(round(inet.download(), 2))[1]) * 0.125
        # self.uploads_MB_S = float(str(inet.upload())[0:2] + "."   # Исходящая скорость
        #                      + str(round(inet.download(), 2))[1]) * 0.125
        self.disks_info = self.disksInfo(self)

    @staticmethod
    def getMac():
        tmp = str(bin(get_mac()))[2:]
        print(tmp)
        tmp2 = []

        # С конца строки по 8 бит записываем адрес
        for i in range(len(tmp), 0, -8):
            print(i)
            if(i >= 8):
                tmp2.append(str(hex(int(tmp[i-8: i], 2)))[2:])
            else:
                tmp2.append(str(hex(int(tmp[0: i], 2)))[2:])

        # Разворачиваем массив тк заполняли его с конца. и формируем строку
        tmp2 = ':'.join(tmp2[::-1])

        return tmp2

    @staticmethod
    def osInfo():
        ost = platform.uname()
        return f'OS={ost.system}_{ost.release}_{ost.machine}'

    @staticmethod
    def cpuInfo():
        psutil.cpu_freq()
        # print(psutil.cpu_stats())

    @staticmethod
    def disksInfo(self):
        tmp = ""
        disks = psutil.disk_partitions(all=True)
        for d in disks:
            tmp += f';{d.device}{self.diskCapacity(d.device)}'
            # print(f'{d.device}{self.diskCapacity(d.device)};')
        return tmp

    # Вспомогательный метод для
    @staticmethod
    def diskCapacity(disk):
        try:
            disk_C = psutil.disk_usage(disk)
            disk_C_total_GB = round(disk_C[0]/1024/1024/1024)
            disk_C_free_GB = round(disk_C[2]/1024/1024/1024)
            disk_C_percent = disk_C[3]
            info_C = f'/{disk_C_free_GB}_GB free of {disk_C_total_GB}_GB Usage_%:{disk_C_percent}'
            return info_C
        except:
            return " Disk is unavailable"


# Принимаем токен (строка) и id-бота (отрицательное число)
# sys.argv[1] и sys.argv[2]
# sys.argv[0] - это название файла
# адрес сервера встроить в код или принимать аргументом
if __name__ == "__main__":
    # obj = DataCollector()#Убрать после тестов

    if (len(sys.argv) == 4):
        args = Args(sys.argv[1], sys.argv[2])
        if(args.isCorrectArgs()):
            print("it`s all right")
            # Теперь вызываем функцию сбора данных а затем отправки на сервер
            obj = DataCollector()
            obj.token = sys.argv[1]
            obj.bot_id = sys.argv[2]
            x = json.dumps(obj.__dict__)
            # Принимать ещё одним аргуменотм?
            requests.post(sys.argv[3], json=x)
        else:
            print("Incorrect arguments. Remember, TOKEN - ID - IP ...")
    else:
        print("Incorrect number of arguments")
