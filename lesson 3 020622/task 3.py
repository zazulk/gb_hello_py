# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(numb_1, numb_2, numb_3):
    """Возвращает сумму наибольших двух аргументов

    :param float numb_1: первый аргумент
    :param float numb_2: второй аргумент
    :param float numb_3: третий аргумент
    :return dict: словарь, содержащий аргументы, которые суммировали, и их сумму
    """
    args = [numb_1, numb_2, numb_3]
    if not all([type(x) is float for x in args]):
        return None
    args.remove(min(args))
    return {"numbs": args, "sum": sum(args)}


stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
try:
    numbs = []
    while len(numbs) != 3:
        inp = input("Нужно ввести ТРИ разных числа через пробел или "
                    "'Q' для выхода: ").replace(",", ".")
        if inp in stop_words:
            print("Ну и ладно :(")
            stop = True
            break
        if not all([y.isdigit() for y in inp.replace('-', '').replace(
                '.', '').split()]):
            print("⚠️ В вводе есть не только цифры и разделитель для "
                  "дробных чисел.")
            numbs = []
            continue
        numbs = inp.split()
        if len(numbs) != len(set(numbs)):
            print(f"{'⚠️':>5}️ Несколько чисел совпадают.")
            numbs = []
    if not stop:
        numbs = list(map(float, numbs))
        result = my_func(numbs[0], numbs[1], numbs[2])
        if result:
            text_sum = ' + '.join(map(str, result['numbs']))
            print(f"Сумма наибольших двух чисел {text_sum} = {result['sum']}")
        else:
            print("Что-то пошло не так.")
except Exception as err:
    print(f"Что-то пошло не так. Ошибка: {err}")
