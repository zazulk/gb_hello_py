# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Вариант 2: пользователь задает кол-во слагаемых,
# используем умножение строк

print("Введите данные.")
numb_inp = ""
max_count = 0

while not numb_inp:
    numb_inp = input(f"{'':>5}Число: ")
    if int(numb_inp) < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {numb_inp} "
              f"положительным.")
        numb_inp = str(int(numb_inp) * -1)
    if int(numb_inp) == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        numb_inp = ""

while not max_count:
    max_count = int(input(f"{'':>5}Количество слагаемых: "))
    if max_count == 0:
        print(f"{'':>7}❌ 0 не принимается.")
    if max_count < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {max_count} "
              f"положительным.")
        max_count *= -1

# Будем собирать выражение суммы текстом, если слагаемых <= 10
text = ""
if max_count <= 10:
    text = numb_inp

result = 0
i = 1
while i <= max_count:
    if text and i > 1:
        text += " + " + numb_inp * i
    result += int(numb_inp * i)
    i += 1

if text:
    print(f"{text} = {result}")
else:
    print(f"Будет {result}")

