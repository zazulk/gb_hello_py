from random import randint
import sys
import time


class Stationery:
    title = "Скрепка"

    def __init__(self, title):
        self.title = title

    def draw(self, n):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self, n):
        print(f"\033[34m{'_' * n}🖊\033[0m {self.title}", end="")


class Pencil(Stationery):
    def draw(self, n):
        print(f"{self.title} \033[37m✏️{'_' * n}\033[0m", end="")


class Handle(Stationery):
    def draw(self, n):
        print(f"\033[31m\033[1m{'_' * n}🖍\033[0m {self.title}", end="")


def drawings_generator(draw_type):
    stationeries = {
        "pen": {
            "titles": ["Bic", "Pilot", "Erich Krause"],
            "class": Pen
        },
        "pencil": {
            "titles": ["Faber-Castell", "Koh-i-Noor", "DALER ROWNEY"],
            "class": Pencil
        },
        "handle": {
            "titles": ["COPIC", "CKETCHMARKER", "TOUCH"],
            "class": Handle
        }
    }
    res_type = stationeries.get(draw_type)
    res_titles = res_type.get("titles")
    for el in res_titles:
        example = res_type.get("class")(el)
        yield example


for drawing in ["pen", "pencil", "handle"]:
    draw_items = drawings_generator(drawing)
    for item in draw_items:
        item.draw(randint(3, 20))
        time.sleep(1)
        sys.stdout.write('\r\x1b[2K')
