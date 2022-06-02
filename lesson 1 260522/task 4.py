# Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.

numb_inp = ""
# Не знаю, как проверить, целое ли, доступными способами
while not numb_inp:
    numb_inp = int(input("Введите целое положительное число: "))
    if numb_inp < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {numb_inp} "
              f"положительным.")
        numb_inp = numb_inp * -1
        break
    if numb_inp == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        continue

numb = numb_inp
max_dig = 0

while numb // 10 >= 0:
    # если это итерация после того, как прошли последнюю цифру, выходим
    if numb // 10 == 0 and numb == 0:
        break
    last_dig = numb % 10
    numb = numb // 10
    if last_dig > max_dig:
        max_dig = last_dig
    if max_dig == 9:
        break

print(f"У числа {numb_inp} самая большая цифра: {max_dig}")
