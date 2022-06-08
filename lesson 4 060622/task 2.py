# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

from random import sample

numbs = list(map(abs, sample(range(-20, 20), 20)))
print("Я выбрал такой список чисел:")
print(f"{'':>8}{numbs}")
result = [n for n in numbs if 0 <= numbs.index(n) - 1 < len(numbs) and numbs[
    numbs.index(n) - 1] < n]
print("Элементы этого списка, значения которых больше предыдущего элемента:")
print(f"{'':>8}{result}")
