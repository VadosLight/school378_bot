# Телеграм бот для отслеживания состояния компьютеров

> Server py - это серверный файл, который запускает бота,
> а также слушает определенный порт, чтобы получать сообщения
> от контролируемых компьютеров.

> dataCollector py - это клиентский файл, который с определенной
> периодичностью отпаравляет на сервер данные о прослушиваемом устройстве.

> Компиляция происходит через auto-py-to-exe с параметром --onefile

### Инструкция

1) Запустить server(py/exe) на сервере, на адрес которого смогут делать запрос клиенты. (Внешний ip или единая локальная сеть)
2) Поместить на нужные ПК скрипт/утилиту (dataCollector.exe и Ярлык с параметрами) параметры вида "TOKEN" "BOT_ID" "SERVER_IP:PORT"
    - (Windows) Поле Target ярлыка должно содержать %windir%\system32\cmd.exe /C start .\dataCollector.exe "TOKEN" "BOT_ID" "SERVER_IP:PORT"
    - (Linux) Ярлык не требуется. Запускаем сам исполняемый файл с параметрами "TOKEN" "BOT_ID" "SERVER_IP:PORT"
3) Добавить в планировщик задач ссылку на ЯРЛЫК (Windows) или Исполняемый файл (Linux)


## Что почитать

- https://jenyay.net/Programming/Argparse
- https://python-scripts.com/requests#install-requests
- https://ru.stackoverflow.com/questions/1138286/%D0%9E%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D0%B1%D0%BE%D1%82%D0%B0
- https://mastergroosha.github.io/telegram-tutorial/docs/lesson_01/
- https://pypi.org/project/pyTelegramBotAPI/0.3.0/
- https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html
- https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
- https://coderoad.ru/40233123/Windows-Defender-%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BF%D0%B0%D0%BF%D0%BA%D1%83-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B9-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE
- https://www.geeksforgeeks.org/append-to-json-file-using-python/
- https://stackoverflow.com/questions/159137/getting-mac-address
- https://www.tutorialspoint.com/How-to-convert-string-to-JSON-using-Python
- https://docs.python.org/3/library/functions.html#dir
- https://psutil.readthedocs.io/en/latest/#psutil.disk_partitions

---
## Библиотеки

- pip install pyTelegramBotAPI requests auto-py-to-exe psutil speedtest
