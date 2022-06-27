from random import uniform
from random import randint
from random import choice


class ComplexNumb:
    def __init__(self, a, b):
        self.value = complex(round(a, 2), round(b, 2))
        self.a = round(a, 2)
        self.b = round(b, 2)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumb(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.a * other.b + other.a * self.b
        return ComplexNumb(new_a, new_b)

    def __str__(self):
        return str(self.value)


for i in range(5):
    i += 1
    cmp_n_1 = ComplexNumb(choice([uniform(-10, 10), randint(-10, 20)]),
                          choice([uniform(-10, 10), randint(-10, 20)]))
    cmp_n_2 = ComplexNumb(choice([uniform(-10, 10), randint(-10, 20)]),
                          choice([uniform(-10, 10), randint(-10, 20)]))
    print(f"{cmp_n_1} + {cmp_n_2} = {cmp_n_1 + cmp_n_2}")
    print(f"{cmp_n_1} * {cmp_n_2} = {cmp_n_1 * cmp_n_2}")
    cmp_n_3 = ComplexNumb(choice([uniform(-10, 10), randint(-10, 20)]),
                          choice([uniform(-10, 10), randint(-10, 20)]))
    print(f"{cmp_n_1} + {cmp_n_2} + {cmp_n_3} = {cmp_n_1 + cmp_n_2 + cmp_n_3}")
    print(f"{cmp_n_1} * {cmp_n_2} * {cmp_n_3} = {cmp_n_1 * cmp_n_2 * cmp_n_3}")
    print("-"*30)
