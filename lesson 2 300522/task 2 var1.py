# Для списка реализовать обмен значений соседних элементов. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном
# количестве элементов последний сохранить на своём месте. Для заполнения
# списка элементов нужно использовать функцию input().

inp = input("Скажите что-нибудь: ")
list_inp = inp.split()
if len(list_inp) == 1:
    print("Этого мало.")
    inp += " " + input("Еще что-нибудь скажите: ")
    list_inp = inp.split()

for k in range(len(list_inp)):
    if (k+1) % 2 == 0:
        print(f"k = {k}")
        actual = list_inp[k]
        last = list_inp[k-1]
        list_inp[k-1], list_inp[k] = actual, last

print(" ".join(list_inp))
