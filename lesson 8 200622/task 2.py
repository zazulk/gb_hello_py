from random import randint


class ZeroException(ZeroDivisionError):
    def __init__(self, msg):
        super().__init__(f"⛔️ {msg}")


rand_n = randint(1, 100)
inp = input(f"На что поделим {rand_n}: ")

if inp:
    try:
        div_n = int(inp)
        if div_n == 0:
            raise ZeroException("Вам тут не алгебра колёс, на ноль делить "
                                "нельзя!")
    except ZeroException as my_err:
        print(my_err)
    except ValueError:
        print("⛔ Вы ввели какую-то хрень.")
    else:
        print(f"{rand_n} / {div_n} = {rand_n / div_n}")


