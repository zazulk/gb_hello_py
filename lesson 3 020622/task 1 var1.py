# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def div(n1, n2):
    """Делит перове число на второе

    :param float n1:
    :param float n2:
    :return float:
    """
    if n2 == 0:
        return 0
    return n1 / n2


stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
result = None

while not stop and result is None:
    inp = input("Введите два числа для деления или 'Q' для выхода: ")
    if inp.strip() in stop_words:
        print("Ну и ладно :(")
        stop = True
        break
    try:
        args = list(map(float, inp.split()))
        print(f"args = {args}")
    except Exception:
        args = None
    if not args:
        if args is None:
            print(f"{'❌':>5} Введены некорректные данные.")
        continue
    if len(args) == 0:
        continue
    if len(args) != 2:
        print(
            f"{'⚠️':>5} Вы ввели {'более' if len(args) > 2 else 'менее'} двух чисел.")
        continue
    result = div(args[0], args[1])


if not stop:
    if result == 0:
        print(f"Делить на 0 нельзя. Учите матчасть.")
    else:
        round_res = round(result, 2)
        if round_res == result:
            print(f"Результат: {result}")
        else:
            print(f"Результат (округлил): {round_res}")
