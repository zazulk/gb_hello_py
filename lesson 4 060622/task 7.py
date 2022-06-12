# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за
# получение факториала числа. В цикле нужно выводить только первые n чисел,
# начиная с 1! и до n!.

from my_funcs import is_stop
from my_funcs import get_numb_from_user


def fact(num):
    """Генератор списка чисел от одного до переданного

    :param int num: число
    :rtype: generator
    """
    res = 1
    start = 0
    if num == 0:
        start = 0
    for i in range(start, num + 1):
        yield f'{i}! = {res}'
        res *= i + 1


quest = "Введите целое число или 'Q' для выхода:"
n = get_numb_from_user(quest, kind_of_numb="int", positive=True, negative=True)

if n is not None:
    for el in fact(n):
        print("-" * 20)
        print(f"{el}")
