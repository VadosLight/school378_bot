import os
import sys
import requests
import json
import ssd
import getpass
import socket
import psutil
import platform
import uuid
import cpuinfo
import wmi
from datetime import datetime
from speedtest import Speedtest
inet = Speedtest()

# Знак ";" служит как символ новой строки.
# <celsius> = °


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
        network = psutil.net_if_addrs()
        lanInfo = ""

        try:
            LAN = network["Ethernet"][0].address
            lanInfo += f';MAC_LAN={LAN}'
        except:
            print()

        try:
            W_LAN = network["Беспроводная сеть"][0].address
            lanInfo += f';MAC_WLAN={W_LAN}'
        except:
            print()

        return lanInfo

    @staticmethod
    def osInfo():
        ost = platform.uname()
        return f'OS={ost.system}_{ost.release}_{ost.machine}'

    @staticmethod
    def cpuInfo():
        cpuBrand = cpuinfo.get_cpu_info()["brand_raw"]

        try:
            w = wmi.WMI(namespace="root\wmi")
            temp_info = round(w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10 -273)
        except:
            temp_info = "Access_denied"

        print(f';{cpuBrand} ({temp_info}°C)')
        return f';{cpuBrand} ({temp_info}<celsius>C)'

    @staticmethod
    def disksInfo(self):
        tmp = ""
        type_drive = ""
        disks = psutil.disk_partitions(all=True)
        for d in disks:
            disk_name = d.device.replace("\\", "/")
            try:
                if ssd.is_ssd(disk_name):
                    type_drive = "SSD"
                else:
                    type_drive = "HDD"
            except:
                type_drive = "Not defined"

            tmp += f';{disk_name}_{type_drive}_{self.diskCapacity(disk_name)}'
            # print(f';{disk_name}_{type_drive}_{self.diskCapacity(disk_name)}')
        return tmp

    # Вспомогательный метод для disksInfo
    @staticmethod
    def diskCapacity(disk):
        try:
            disk_C = psutil.disk_usage(disk)
            disk_C_total_GB = round(disk_C[0]/1024/1024/1024)
            disk_C_free_GB = round(disk_C[2]/1024/1024/1024)
            disk_C_percent = disk_C[3]
            info_C = f'{disk_C_free_GB}_GB free of {disk_C_total_GB}_GB Usage_%:{disk_C_percent}'
            return info_C
        except:
            return " Disk is unavailable"


# Принимаем токен (строка) и id-бота (отрицательное число)
# sys.argv[1] и sys.argv[2]
# sys.argv[0] - это название файла
# адрес сервера встроить в код или принимать аргументом
if __name__ == "__main__":
    # obj = DataCollector()  # Убрать после тестов

    if (len(sys.argv) == 4):
        args = Args(sys.argv[1], sys.argv[2])
        if(args.isCorrectArgs()):
            print("it`s all right")
            # Теперь вызываем функцию сбора данных а затем отправки на сервер
            obj = DataCollector()
            obj.token = sys.argv[1]
            obj.bot_id = sys.argv[2]
            x = json.dumps(obj.__dict__)
            requests.post(sys.argv[3], json=x)
        else:
            print("Incorrect arguments. Remember, TOKEN - ID - IP ...")
    else:
        print("Incorrect number of arguments")
