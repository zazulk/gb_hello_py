# Программа принимает действительное положительное число x и целое
# отрицательное число y. Выполните возведение числа x в степень y. Задание
# реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись
# без встроенной функции возведения числа в степень.

def my_func(x, y):
    """Возвращает возведение числа x в степень y

    :param float x: действительное положительное число
    :param int y: целое отрицательное число
    :return:
    """
    if x <= 0 or type(y) is not int or y >= 0:
        return None
    return pow(x, y)


stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
n1 = 0
n2 = 0
inp = ""

print("Будем возводить положительное число в отрицательную степень.")
while not n1 or not n2:
    if not n1:
        inp = input("Введите действительное положительное число или "
                    "'Q' для выхода: ").replace(",", ".").strip()
        if not inp:
            continue
        if inp in stop_words:
            print("Ну и ладно :(")
            stop = True
            break
        if not inp.replace("-", "").isdigit() or float(inp) <= 0:
            print(f"{'⚠️':>8} Это должно быть действительное положительное "
                  f"число.")
            n1 = 0
            continue
        n1 = float(inp)
    if not n2:
        inp = input("Введите целое отрицательное число или 'Q' для выхода: ").\
            replace(",", ".").strip()
        if not inp:
            continue
        if inp in stop_words:
            print("Ну и ладно :(")
            stop = True
            break
        if not inp.replace("-", "").isdigit() or inp.count(".") or \
                int(inp) >= 0:
            print(f"{'⚠️':>8} Это должно быть целое отрицательное число.")
            n2 = 0
            continue
        n2 = int(inp)

if not stop:
    result = my_func(n1, n2)
    round_res = result and round(result, 3)

    if result and round_res == result:
        print(f"\n{n1} в степени {n2} = {result}")
    elif not result:
        print("Что-то пошло не так...")
    else:
        print(f"\n{n1} в степени {n2} (округлил) = {round_res}")
