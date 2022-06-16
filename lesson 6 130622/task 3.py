from random import choice
from random import randint


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


names_m = ["Василий", "Петр", "Захар", "Иван"]
surnames_m = ["Иванов", "Петров", "Лопатин", "Троян"]
positions = ["дворник", "оператор цеха", "секретарь", "охранник"]

postman = Position(choice(names_m), choice(surnames_m), choice(positions),
                   randint(30000, 90000), randint(3000, 10000))
print(f"Знакомьтесь - {postman.get_full_name()}! Доход в месяц: "
      f"{postman.get_total_income()}руб.")
