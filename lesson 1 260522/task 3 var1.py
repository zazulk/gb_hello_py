# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Вариант 1: для конкретной задачи с 3мя слагаемыми

n = ""
while not n:
    n = input("Назовите число: ")
    if int(n) < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {n} "
              f"положительным.")
        n = str(int(n) * -1)
    if int(n) == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        n = ""

text = f"{n} + {n + n} + {n + n + n}"
result = int(n) + int(n + n) + int(n + n + n)

print(f"{text} = {result}")