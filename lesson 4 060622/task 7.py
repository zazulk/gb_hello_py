# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за
# получение факториала числа. В цикле нужно выводить только первые n чисел,
# начиная с 1! и до n!.

from my_funcs import is_stop
from my_funcs import is_float_numb
from my_funcs import is_numb_str


def fact(num):
    for elem in range(1, num + 1):
        yield elem


numb_inp = ""
n = 0

while not numb_inp:
    numb_inp = input(f"Введите целое число или 'Q' для выхода: ").strip()
    if numb_inp == "":
        continue
    if is_stop(numb_inp):
        stop = True
        break
    if is_float_numb(numb_inp) or not is_numb_str(numb_inp):
        print(f"{'⚠️':>5} Некорректное число.")
        continue
    n = int(numb_inp)

res = 1
for el in fact(n):
    print("-" * 20)
    print(f"el = {el}")
    res = res * el
    print(f"Факториал {el} = {res}")
