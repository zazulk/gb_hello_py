# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.

# Вариант 2: без break

from itertools import count
from itertools import cycle
from itertools import islice
from my_funcs import is_stop
from my_funcs import is_float_numb
from my_funcs import is_numb_str
import random

print("Вводите данные или 'Q' для выхода.")

start_n = 0
max_count = 0
try_count = 0
result = []
stop = False

while not start_n:
    numb_inp = input(f"{'':>4} целое число, начиная с которого будем "
                     f"генерировать: ").strip()
    if numb_inp == "":
        continue
    if is_stop(numb_inp):
        stop = True
        break
    if is_float_numb(numb_inp) or not is_numb_str(numb_inp):
        print(f"{'⚠️':>8} Нужно вводить целые числа.")
        continue
    start_n = int(numb_inp)
    if start_n == 0:
        break

if stop:
    print("Ну и ладно :(")

if not stop:
    while not max_count:
        if try_count >= 3:
            max_count = random.randint(5, 15)
            print(f"{'':>5}Так, ладно, сам выберу. Сгенерирую {max_count} чисел.")
            break
        max_inp = input(f"{'':>5}сколько чисел сгенерировать: ").strip()
        if not max_inp:
            try_count += 1
            continue
        if is_stop(max_inp):
            stop = True
            break
        if is_float_numb(max_inp) or not is_numb_str(max_inp):
            try_count += 1
            print(f"{'⚠️':>8} Нужно вводить целые числа.")
            continue
        max_count = int(max_inp)
        if max_count <= 0:
            max_count = 0
            try_count += 1
            print(f"{'⚠️':>8} Количество не может быть нулем или "
                  f"отрицательным.")
            continue

    gen_count = count(start_n)
    while len(result) != max_count:
        n = next(gen_count)
        result.append(n)
        print(n)

    print(f"\n✅ Итого: {', '.join(map(str, list(islice(count(start_n), max_count))))}")

print("*" * 30)

phrase = "Делу время, потехе час"
words = [w.upper().replace(",", "") for w in phrase.split()]
limit = random.randint(round(len(words) * 1.5), round(len(words) * 2.5))
print(f"🆎 А сейчас я буду повторять слова из фразы «{phrase}».")

gen_cycle = cycle(words)
c = 0
while c != limit:
    print(next(gen_cycle))
    c += 1
