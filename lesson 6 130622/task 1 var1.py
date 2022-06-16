import time
from random import randint


class TrafficLight:
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
        while result <= limit_secs:
            for key, value in self.__colors.items():
                print(f"{value.get('txt_color')} {key}")
                time.sleep(value.get("pause"))
                result = time.monotonic() - start


traffic_lighter = TrafficLight()
traffic_lighter.running(randint(20, 50))

