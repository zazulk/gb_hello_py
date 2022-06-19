import time
from random import randint
import sys

# Вариант 1. Перемещаемся туда сюда по строкам терминал и печатаем кружочки
# ⚠️ Нужно включить настройку "Emulate terminal in output console"


class TrafficLight:
    __color = "yellow"
    __colors = {
        "red": {
            "pause": 7,
            "emoji": "🔴"
        },
        "yellow": {
            "pause": 2,
            "emoji": "🟡"
        },
        "green": {
            "pause": randint(4, 7),
            "emoji": "🟢"
        },
    }

    def running(self, limit_secs=30):
        if type(limit_secs) is not int:
            return
        start = time.monotonic()
        result = 0
        colors = list(self.__colors.keys())
        colors.append(self.__color)
        # count = 0
        while result <= limit_secs:
            for color in colors:
                # Если не хотим, чтобы криво отображался первый кружочек 😬
                # count += 1
                # if color == "red" and count > 1:
                if color == "red":
                    sys.stdout.write('\r\x1b[2A')

                color_info = self.__colors.get(color)
                print(f"{color_info.get('emoji')}", end='')
                time.sleep(color_info.get("pause"))
                sys.stdout.write('\r\x1b[2K')
                print(f"\r⚫️")
                if color == "green":
                    sys.stdout.write('\x1b[2F')
                result = time.monotonic() - start

        sys.stdout.write('\x1b[2B')


traffic_lighter = TrafficLight()
traffic_lighter.running(randint(20, 50))
