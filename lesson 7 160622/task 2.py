from abc import ABC, abstractmethod
from random import uniform
from random import randint
from random import choice
from itertools import chain


class Clothing(ABC):

    def __init__(self, name, param):
        if type(name) is not str or type(param) not in [int, float]:
            raise ValueError(name, param)
        self.name = name
        self.param = param

    @abstractmethod
    def tissue_amount(self):
        pass

    def __str__(self):
        return f"name:{self.name}\n\tparam: {self.param}\n\ttissue_amount: " \
               f"{self.tissue_amount}"


class Coat(Clothing):

    @property
    def tissue_amount(self):
        return round(self.param / 6.5 + 0.5, 2)

    def __str__(self):
        return f"🧥Пальто \"{self.name}\"\n\tразмер: {self.param}\n\t" \
               f"расход ткани: {self.tissue_amount}"


class Costume(Clothing):

    def __init__(self, name, param):
        if type(param) is not float:
            param = param / 100
        super().__init__(name, param)

    @property
    def tissue_amount(self):
        return round(2 * self.param + 0.3, 2)

    def __str__(self):
        return f"🥼Костюм \"{self.name}\"\n\tрост: {self.param}\n\tрасход " \
               f"ткани: {self.tissue_amount}"


def produce_clothes():
    coat_names = ["Редингот", "Шинель", "Реглан", "Кейп"]
    costume_names = ["Тройка", "Двойка"]

    new_costumes = [Costume(costume_name, choice([round(uniform(1.3, 2.3), 2),
                                                  randint(145, 230)])) for
                    costume_name in
                    costume_names[:randint(1, len(costume_names))]]
    new_coats = [Coat(coat_name, randint(40, 58)) for coat_name in
                 coat_names[:randint(1, len(coat_names))]]

    new_clothes = list(chain(new_costumes, new_coats))

    print(f"Пошил вот:\n")
    for clothing in new_clothes:
        print(clothing)

    print(f"\nЗатратил {sum([el.tissue_amount for el in new_clothes])}м ткани.")


produce_clothes()
