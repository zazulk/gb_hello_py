# Для списка реализовать обмен значений соседних элементов. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном
# количестве элементов последний сохранить на своём месте. Для заполнения
# списка элементов нужно использовать функцию input().


inp = input("Я переставлю слова местами. Скажите что-нибудь: ").strip()
stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False

while len(inp) <= 1:
    if inp in stop_words:
        print("Ну и ладно :(")
        stop = True
        break
    if len(inp) == 0:
        inp = input("Скажите что-нибудь или введите 'Q' для выхода: ")
    if len(inp) == 1:
        print("⚠️ Этого мало.")
        inp += " " + input("Еще что-нибудь скажите: ")

if not stop:
    words = inp.strip().split()

    for ind in range(len(words)):
        if (ind + 1) % 2 == 0:
            actual = words[ind]
            last = words[ind-1]
            words[ind-1], words[ind] = actual, last

    print("Результат перестановки слов:")
    print(" ".join(words))
