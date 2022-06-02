# Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10%
# относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное число —
# номер дня.

print("Введите начальные данные.")

km_1 = 0
while not km_1:
    km_1 = float(input(f"{'':>5}Результат пробежки в 1-й день: "))
    if km_1 < 0:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {km_1} "
              f"положительным.")
        km_1 *= -1
        break
    if km_1 == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        continue

km_max = 0
while not km_max:
    km_max = float(input(f"{'':>5}Желаемый результат: "))
    if km_max < 0 and km_max * -1 > km_1:
        print(f"{'':>7}Отрицательные числа не принимаются. Сделаю {km_max} "
              f"положительным.")
        km_max *= -1
        break
    if km_max < 0 and km_max * -1 < km_1:
        print(f"{'':>7}Отрицательные числа не принимаются. "
              f"Нужно стремиться к прогрессу.")
        km_max = 0
        continue
    if km_max == 0:
        print(f"{'':>7}❌ 0 не принимается.")
        continue
    if km_max < km_1:
        print(f"{'':>7}❌ {km_max} меньше {km_1}. Нужно стремиться к прогрессу.")
        km_max = 0
        continue
    if km_max == km_1:
        print(f"{'':>7}❌ Нужно стремиться к прогрессу.")
        km_max = 0
        continue

visible_count = input(f"{'':>5}Показывать динамику расчета? "
                      f"Введите \"да\" или \"нет\": ")

day_numb = 0
km_per_day = 0

while km_per_day < km_max:
    if km_per_day == 0:
        km_per_day = km_1
    else:
        km_per_day += km_per_day * 0.1
    day_numb += 1
    if visible_count == "да" or visible_count == "Да" or visible_count == "ДА":
        print(f"{day_numb}-й день: {km_per_day:.2f}")

print(f"\nРезультат не менее {km_max}км будет достигнут на {day_numb}-й день.")