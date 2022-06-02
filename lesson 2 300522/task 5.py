# Реализовать структуру «Рейтинг», представляющую собой набор натуральных
# чисел, который не возрастает. У пользователя нужно запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после
# них.

rating = []
full_rating = list(range(1, 11))
full_rating.reverse()

variants = [
    [7, 4],
    [5],
    [9, 6, 1],
    full_rating,
]
stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False

print("Варианты рейтинга для тестирования:")
for num, elem in enumerate(variants, 1):
    print(num, elem)

choice_inp = input("Назовите номер варианта из списка:")
choice_int = 0
try_count = 0
var_int_list = list(range(1, len(variants)))
var_numbers = str(var_int_list).replace(",", "").replace("[", "").replace(
        "]", "").split()
while choice_inp not in var_numbers:
    try_count += 1
    if choice_inp in stop_words:
        stop = True
        print("Ну и ладно.")
    elif try_count > 2:
        print("Ну и ладно. Сам выбрал.")
        choice_int = len(variants)
        break
    else:
        choice_inp = input("Я настаиваю. Номер варианта из списка:")

choice_int = choice_int if choice_int else int(choice_inp)
rating = variants[choice_int - 1]
print(f"{'Ваш' if try_count <= 2 else 'Мой'} выбор: {rating}")
print("Вводите натуральные числа, а я буду добавлять их в рейтинг.")

while not stop:
    new_item = input(f"{'':>5}Число или \"Q\" (для выхода): ")
    if new_item.lower() in stop_words:
        stop = True
        print("Закончили.")
    else:
        rating.append(int(new_item))
        rating.sort(reverse=True)
        print(f"Новое состояние рейтинга: {rating}")

