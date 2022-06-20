from random import randint
from random import randrange
from random import uniform
from random import choice


class CellException(Exception):
    def __init__(self, message=None, value=None):
        self.message = message
        self.value = value
        if message and not value:
            super().__init__(f"⛔️ {message}")

    def __str__(self):
        if not isinstance(self.value, int):
            return "⛔️ Количество ячеек должно быть целым положительным числом."
        elif self.value < 0:
            return "⛔️ Невозможно создать клетку с отрицательным числом ячеек."
        elif self.value == 0:
            return "⛔️ Невозможно создать клетку без ячеек."
        else:
            return "⛔️ Что-то не так"


class Cell:

    def __init__(self, amount):
        if type(amount) is int and amount > 0:
            self.amount = amount
        else:
            raise CellException(value=amount)

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        sub_res = self.amount - other.amount
        if sub_res > 0:
            return Cell(sub_res)
        else:
            raise CellException(sub_res)

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        div_res = self.amount // other.amount
        if div_res > 0:
            return Cell(div_res)
        else:
            raise CellException(div_res)

    def __str__(self):
        return f"{'▫️' * self.amount}"

    def make_order(self, n):
        if not isinstance(n, int) or n <= 0:
            print("⛔️ Количество ячеек в ряду должно быть целым положительным "
                  "числом.")
        full_rows_numb = self.amount // n
        last_row_numb = self.amount % n
        one_raw = '▫️' * n + '\n'
        return f"{one_raw * full_rows_numb}{'▫️' * last_row_numb}"


def generate_cells(numb_of_cells):
    cells = []
    for i in range(1, numb_of_cells + 1):
        # new_cell = Cell(choice([randint(-1, 30), uniform(2.0, 5.0)]))
        new_cell = Cell(randint(-1, 30))
        cells.append(new_cell)
        print(f"{i}) {new_cell}")
        rand_count = randint(1, 15)
        print(f"Выводим по {rand_count} в ряду:\n{new_cell.make_order(rand_count)}\n")

    for ind, item in enumerate(cells, 1):
        for el in ["add", "mul", "sub", "div"]:
            rand_ind = randrange(len(cells))
            if el == "add":
                print(f"Складываем клетку {ind} с клеткой {rand_ind}: {item + cells[rand_ind]}")
            if el == "mul":
                print(f"Вычитаем из клетки {ind} клетку {rand_ind}: {item - cells[rand_ind]}")
            if el == "mul":
                print(f"Умножаем клетку {ind} на клетку {rand_ind}: {item * cells[rand_ind]}")
            elif el == "div":
                print(f"Делим клетку {ind} на клетку {rand_ind}: {item / cells[rand_ind]}")


generate_cells(randint(5, 10))
