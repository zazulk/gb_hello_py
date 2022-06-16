import time
from random import randint


class TrafficLight:
    __color = "yellow"
    __colors = {
        "red": {
            "pause": 7,
            "txt_color": "\033[31m🔴"
        },
        "yellow": {
            "pause": 2,
            "txt_color": "\033[33m🟡"
        },
        "green": {
            "pause": randint(4, 7),
            "txt_color": "\033[32m🟢"
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
                print(f"{color_info.get('txt_color')} {color}")
                time.sleep(color_info.get("pause"))
                result = time.monotonic() - start


traffic_lighter = TrafficLight()
traffic_lighter.running(randint(20, 50))

