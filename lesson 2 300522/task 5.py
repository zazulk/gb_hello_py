# Реализовать структуру «Рейтинг», представляющую собой набор натуральных
# чисел, который не возрастает. У пользователя нужно запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после
# них.

rating = list(range(1, 11))
rating.reverse()
print(rating)

print("Вводите натуральные числа, а я буду добавлять их в свой рейтинг.")
stop = False

while not stop:
    new_item = input(f"{'':>5}Число или \"стоп\": ")
    if new_item.lower() in ["стоп", "stop"]:
        stop = True
        print("Закончили.")
    else:
        new_item = int(new_item)
        for item in rating:
            if item == new_item and rating[rating.index(item) + 1] != new_item:
                rating.insert(rating.index(item) + 1, new_item)
                break
            elif new_item > item:
                rating.insert(rating.index(item) - 1, new_item)
                break
        print(f"Новое состояние рейтинга: {rating}")

