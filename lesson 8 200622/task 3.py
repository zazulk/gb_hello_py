from my_funcs import is_stop
from my_funcs import is_numb_str


class NanException(Exception):
    def __init__(self, val=None):
        super().__init__(f"\t⛔️ {val} - не число!")


numbs = []
inp = None

while not is_stop(inp):
    inp = input(f"Введите число: ")
    if not inp:
        continue
    try:
        if not is_numb_str(inp):
            raise NanException(val=inp)
        numbs.append(float(inp.replace(",", ".")))
    except NanException as err:
        print(err)
    finally:
        print(f"\tnumbs = {numbs}")
