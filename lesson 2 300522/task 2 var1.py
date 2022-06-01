# Для списка реализовать обмен значений соседних элементов. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном
# количестве элементов последний сохранить на своём месте. Для заполнения
# списка элементов нужно использовать функцию input().


inp = input("Скажите что-нибудь: ").strip()

while len(inp) <= 1:
    if len(inp) == 0:
        inp = input("Скажите что-нибудь: ")
    if len(inp) == 1:
        print("⚠️ Этого мало.")
        inp += " " + input("Еще что-нибудь скажите: ")

words = inp.strip().split()

for ind in range(len(words)):
    if (ind + 1) % 2 == 0:
        actual = words[ind]
        last = words[ind-1]
        words[ind-1], words[ind] = actual, last

print("Результат перестановки слов:")
print(" ".join(words))
