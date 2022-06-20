from abc import ABC, abstractmethod
from random import uniform


class Clothing(ABC):
    name = "Одежда"

    @property
    @abstractmethod
    def tissue_amount(self):
        pass


class Coat:
    def __init__(self, name, v):
        if type(name) is not str or type(v) not in [int, float]:
            raise ValueError(name, v)
        self.name = name
        self.v = v

    @property
    def tissue_amount(self):
        return round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f"Пальто \"{self.name}\"\n\tразмер: {self.v}\n\tрасход ткани: " \
               f"{self.tissue_amount}"


class Costume:
    def __init__(self, name, h):
        if type(name) is not str or type(h) not in [int, float]:
            raise ValueError(name, h)
        self.name = name
        self.h = h

    @property
    def tissue_amount(self):
        return round(2 * self.h + 0.3, 2)

    def __str__(self):
        return f"Костюм \"{self.name}\"\n\tрост: {self.h}\n\tрасход ткани: " \
               f"{self.tissue_amount}"


# uniform(1.3, 2.3)

new_costume = Costume("Двойка", 1.69)
new_coat = Coat("Пальте", 44)
print(new_costume)
print(new_coat)

# ["Редингот", "Шинель", "Реглан", "Кейп"]
# ["Тройка", "Двойка"]