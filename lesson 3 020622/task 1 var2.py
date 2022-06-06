# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.


def div(n1, n2):
    """Делит перовое число на второе

    :param float n1:
    :param float n2:
    :return float || str:
    """
    try:
        res = n1 / n2
    except Exception as error:
        res = str(error)
    return res


stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
result = None

while not stop and not result:
    inp = input("Введите два числа для деления или 'Q' для выхода: ")
    if inp.strip() in stop_words:
        print("Ну и ладно :(")
        stop = True
        break
    try:
        args = list(map(float, inp.split()))
    except Exception:
        args = None
    if not args:
        if args is None:
            print(f"{'❌':>5} Введены некорректные данные.")
        continue
    if len(args) == 0:
        continue
    if len(args) != 2:
        print(f"{'⚠️':>5} Вы ввели {'более' if len(args) > 2 else 'менее'} двух чисел.")
        continue
    result = div(args[0], args[1])

if not stop:
    if type(result) is float:
        round_res = round(result, 2)
        if round_res == result:
            print(f"Результат: {result}")
        else:
            print(f"Результат (округлил): {round_res}")
    else:
        print(f"❌ Ошибка: {result}")
