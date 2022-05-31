# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Вариант 3: пользователь задает кол-во слагаемых,
# не используем умножение строк

print("Введите данные.")
numb_inp = ""
max_count = 0

# в отличие от Варианта 2 дополнительно ставим continue в циклах ниже
# мотивация: может так прозрачнее и если код потом дополнять еще условиями
# или поменять условия местами, можно получить ошибку или цикл прекратится
# раньше, чем нужно

while not numb_inp:
    numb_inp = input(f"{'':>5}Число: ")
    if int(numb_inp) < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {numb_inp} "
              f"положительным.")
        numb_inp = str(int(numb_inp) * -1)
        break
    if int(numb_inp) == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        numb_inp = ""
        continue

while not max_count:
    max_count = int(input(f"{'':>5}Количество слагаемых: "))
    if max_count == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        continue
    if max_count < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {max_count} "
              f"положительным.")
        max_count *= -1
        break


# будем менять введенное строчное число
numb_new = numb_inp
# будем наращивать результат, начиная с введенного числа
result = int(numb_inp)
i = 1
# Будем собирать выражение суммы текстом, если слагаемых <= 10
text = ""
if max_count <= 10:
    text = numb_inp

while i < max_count:
    i += 1
    numb_new += numb_inp
    result += int(numb_new)
    if text and i > 1:
        text += " + " + numb_new

if text:
    print(f"{text} = {result}")
else:
    print(f"Будет {result}")
