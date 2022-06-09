# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

from random import sample

numbs = list(map(abs, sample(range(-20, 20), 20)))
print("Я выбрал такой список чисел:")
print(f"\t{numbs}")
result = [n for i, n in enumerate(numbs[1:]) if n > numbs[i]]
print("Элементы этого списка, значения которых больше предыдущего элемента:")
print(f"\t{result}")

