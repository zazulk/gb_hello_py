from random import choice
from random import uniform

forms = ["ЗАО", "ПАО", "ОАО", "АОЗТ", "НАО"]

with open("file for task 7 source.txt", "w+") as file:
    for n in range(1, 21):
        revenue = uniform(10_000, 50_000)
        costs = uniform(5_000, 50_000)
        file.write(f"firm_{n} {choice(forms)} {revenue:.2f} {costs:.2f}\n")

    file.seek(0)
    content = file.read()
    print(f"Содержание файла:\n{content}")
