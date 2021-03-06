# Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма. Например, прибыль — выручка
# больше издержек, или убыток — издержки больше выручки. Выведите
# соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите
# рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на
# одного сотрудника.

print("Введите данные.")
revenue = float(input(f"{'':>5}Выручка: "))
costs = float(input(f"{'':>5}Издержки: "))

profit = revenue - costs
if profit == 0:
    print("Прибыль фирмы нулевая. Пора закрываться или менять процессы.")
elif profit < 0:
    print(f"Фирма терпит значительные убытки {-profit}. "
          f"Пора закрываться или менять процессы.")
else:
    # рентабельность
    profitability = profit / costs * 100
    staff_amount = int(input("Введите число сотрудников:"))
    profit_per_staff_member = profit / staff_amount

    print("\nРезультаты:")
    print(f"{'':>5}Прибыль фирмы: {profit:.2f}")
    print(f"{'':>5}Рентабельность: {profitability:.2f}%")
    print(f"{'':>5}Прибыль на одного сотрудника: {profit_per_staff_member:.2f}")
