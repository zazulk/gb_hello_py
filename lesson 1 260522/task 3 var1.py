# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Вариант 1: для конкретной задачи с 3мя слагаемыми

user_number_inp = input("Назовите число: ")
result = int(user_number_inp) + int(user_number_inp * 2) + int(
    user_number_inp * 3)
print(result)
