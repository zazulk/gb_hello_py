import time
from random import randint
import sys

# Вариант 2. Все кружочки одна строка
# ⚠️ Нужно включить настройку "Emulate terminal in output console"


class TrafficLight:
    __color = "yellow"
    __colors = {
        "red": {
            "pause": 7,
            "lighter": "🔴\n⚫️\n⚫️"
        },
        "yellow": {
            "pause": 2,
            "lighter": "⚫️\n🟡\n⚫️"
        },
        "green": {
            "pause": randint(4, 7),
            "lighter": "⚫️\n⚫️\n🟢"
        },
    }

    def running(self, limit_secs=30):
        if type(limit_secs) is not int:
            return
        start = time.monotonic()
        result = 0
        colors = [self.__color]
        colors.extend(list(self.__colors.keys()))

        while result <= limit_secs:
            for color in colors:
                color_info = self.__colors.get(color)
                print(f"\r{color_info.get('lighter')}", end="")
                time.sleep(color_info.get("pause"))
                sys.stdout.write('\r\x1b[2A')
                result = time.monotonic() - start
        sys.stdout.write('\x1b[2B')


traffic_lighter = TrafficLight()
traffic_lighter.running(randint(20, 50))

