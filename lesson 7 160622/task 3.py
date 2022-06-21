from random import randint
from random import randrange
from random import uniform
from random import choice


class CellException(Exception):
    def __init__(self, msg=None, value=None):
        self.msg = msg
        self.value = value
        if msg and not value:
            super().__init__(f"⛔️ {msg}")

    def __str__(self):
        val = f"⛔ Некорректное значение {self.value}."
        if not isinstance(self.value, int):
            return f"{val} Количество ячеек должно быть целым положительным " \
                   f"числом."
        elif self.value < 0:
            return f"{val}️ Невозможно создать клетку с отрицательным числом " \
                   f"ячеек."
        elif self.value == 0:
            return f"{val}️ Невозможно создать клетку без ячеек."
        else:
            return f"{val}️ Что-то не так"


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
            raise CellException(value=sub_res)

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        div_res = self.amount // other.amount
        if div_res > 0:
            return Cell(div_res)
        else:
            raise CellException(value=div_res)

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __str__(self):
        return f"{'▫️' * self.amount}"

    def make_order(self, n):
        if not isinstance(n, int) or n <= 0:
            return "⛔️ Количество ячеек в ряду должно быть целым " \
                   "положительным числом."
        if self.amount < n:
            return '▫️' * self.amount
        return '\n'.join(
            ['▫️' * n for _ in range(self.amount // n)]) + '\n' + '▫️' * (
                    self.amount % n)


def generate_cells(numb_of_cells):
    cells = []
    for i in range(1, numb_of_cells + 1):
        print(f"{i}) ", end="")
        try:
            new_cell = Cell(choice([randint(1, 10), randint(1, 10),
                                    choice([randint(-1, 0), uniform(2.0, 5.0)])]
                                   ))
            cells.append(new_cell)
            print(f"{new_cell}")
            rand_count = randint(-1, 11)
            print(f"Выводим по {rand_count} в ряду:\n"
                  f"{new_cell.make_order(rand_count)}")
        except Exception as err:
            print(err)
    print("-" * 30)
    for ind, item in enumerate(cells, 1):
        for el in ["+", "*", "-", "//", "/"]:
            rand_ind = randrange(len(cells))
            start_txt = f"Клетка_{ind} ({item.amount}) $$ клетка_{rand_ind} " \
                        f"({cells[rand_ind].amount}) = "
            print(f"{start_txt.replace('$$', el)} ", end="")
            try:
                if el == "+":
                    print(f"{(item + cells[rand_ind]).amount}")
                if el == "*":
                    print(f"{(item * cells[rand_ind]).amount}")
                if el == "-":
                    print(f"{(item - cells[rand_ind]).amount}")
                if el == "//":
                    print(f"{(item // cells[rand_ind]).amount}")
                if el == "/":
                    print(f"{(item / cells[rand_ind]).amount}")
            except Exception as err:
                print(err)


generate_cells(randint(3, 10))
