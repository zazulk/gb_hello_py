# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.

# Вариант 2: без break

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
    gen_count = count(start_n)
    while len(result) != max_count:
        n = next(gen_count)
        result.append(n)
        print(n)

    print(f"\n✅ Итого: {', '.join(map(str, list(islice(count(start_n), max_count))))}")

print("*" * 30)

phrase = "Делу время, потехе час"
words = [w.upper().replace(",", "") for w in phrase.split()]
limit = random.randint(round(len(words) * 1.5), round(len(words) * 2.5))
print(f"🆎 А сейчас я буду повторять слова из фразы «{phrase}».")

gen_cycle = cycle(words)
c = 0
while c != limit:
    print(next(gen_cycle))
    c += 1
