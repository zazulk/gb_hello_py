from random import randint
import time


class Stationery:
    title = "Скрепка"

    def __init__(self, title):
        self.title = title

    def draw(self, n):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self, n):
        print(f"\033[34m{'_' * n}🖊\033[0m")


class Pencil(Stationery):
    def draw(self, n):
        print(f"\033[37m✏️{'_' * n}\033[0m")


class Handle(Stationery):
    def draw(self, n):
        print(f"\033[31m{'_' * n}🖍\033[0m")


for cl in [(Pen, "Ручка"), (Pencil, "Карандаш"), (Handle, "Маркер")]:
    example = cl[0](cl[1])
    example.draw(randint(3, 20))
