# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
# заработной платы сотрудника. Используйте в нём формулу: (выработка в
# часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    production, rate, bonus = list(map(float, argv[1:]))
    print(
        f"Исходные данные:\nвыработка в часах: {production}\nставка в час: {rate}"
        f"\nпремия: {bonus}")
    print(f"\n💰 Зарплата сотрудника = {production * rate + bonus}")
except Exception as err:
    print(f"👾 Что-то пошло не так. Ошибка: {err}")

next_action = input("Введите 'edit', чтобы изменить исходные данные, или 'Q', "
                    "чтобы выйти: ")

if next_action.lower() != "edit":
    print("Fin!")
else:
    try:
        production = float(input("выработка в часах: "))
        rate = float(input("ставка в час: "))
        bonus = float(input("премия: "))
        print(f"\n💰 Зарплата сотрудника = {production * rate + bonus}")
    except Exception as err:
        print(f"👾 Что-то пошло не так. Ошибка: {err}")
