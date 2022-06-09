# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.

# Вариант 1: с break

from itertools import count
from itertools import cycle
from itertools import islice
from my_funcs import get_numb_from_user
import random

print("Вводите данные или 'Q' для выхода.")

max_count = None
quest_1 = "целое число, начиная с которого будем генерировать:"
start_n = get_numb_from_user(quest_1, kind_of_numb="int", positive=True,
                             negative=True)

if start_n is not None:
    max_count = get_numb_from_user("сколько чисел сгенерировать:", try_limit=3,
                                   kind_of_numb="int", positive=True,
                                   negative=False, is_with_zero=False)

if start_n is not None and max_count is not None:
    result = []
    for item in count(start_n):
        result.append(item)
        print(f"{'':>5}{item}")
        if len(result) == max_count:
            break

    print(f"\n✅ Итого: {', '.join(map(str, list(islice(count(start_n), max_count))))}")

print("*" * 30)

phrase = "Делу время, потехе час"
words = [w.upper().replace(",", "") for w in phrase.split()]
limit = random.randint(round(len(words) * 1.5), round(len(words) * 2.5))
print(f"🆎 А сейчас я буду повторять слова из фразы «{phrase}».")

c = 0
for w in cycle(words):
    if c > limit:
        break
    print(w)
    c += 1

