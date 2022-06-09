import random


def is_stop(text):
    """Проверяет, является ли текст стоп-словом

    :param str text:
    :return bool:
    """
    if type(text) is not str:
        return False
    stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
    return bool(text in stop_words)


def is_float_numb(elem):
    if type(elem) is float:
        return True
    if type(elem) is str:
        elem = elem.replace(",", ".")
        return len([ch for ch in elem if ch.isdigit()]) == len(elem) - 1 and \
               elem.count(".") == 1
    return False


def is_numb_str(text):
    text = text.replace(",", ".")
    try:
        float_var = float(text)
        return True
    except Exception:
        return False


def get_numb_from_user(question, try_limit=None, rand_n_min=None,
                       rand_n_max=None, kind_of_numb="int", positive=False,
                       negative=False, is_with_zero=True):
    res_n = None
    if not question:
        return None
    numb_inp = ""
    pos_or_neg_adj_pl = ""

    if positive and not negative:
        pos_or_neg_adj_pl = "положительные"
    elif negative and not positive:
        pos_or_neg_adj_pl = "отрицательные"

    if not rand_n_min and rand_n_min != 0 or rand_n_min >= rand_n_max:
        if negative and not positive:
            rand_n_min = -5.0 if kind_of_numb == "float" else -5
        else:
            rand_n_min = 5.0 if kind_of_numb == "float" else 5
    if not rand_n_max and rand_n_max != 0 or rand_n_min >= rand_n_max:
        if negative and not positive:
            rand_n_max = -15.0 if kind_of_numb == "float" else -15
        else:
            rand_n_max = 15.0 if kind_of_numb == "float" else 15

    kind_adj_pl = "дробные" if kind_of_numb == "float" else "целые"
    try_count = 0

    while not numb_inp:
        if try_limit and try_count >= try_limit:
            if kind_of_numb == "float":
                if all([type(el) is float for el in [rand_n_min, rand_n_max]]):
                    res_n = random.uniform(rand_n_min, rand_n_max)
                else:
                    res_n = random.uniform(5.0, 15.0)
            else:
                if all([type(el) is int for el in [rand_n_min, rand_n_max]]):
                    res_n = random.randint(rand_n_min, rand_n_max)
                else:
                    res_n = random.randint(5, 15)
            print(f"{'':>5}Так, ладно, сам выберу. Выбрал {res_n}.")
            break

        numb_inp = input(f"{question} ").replace(",", ".").strip()
        if numb_inp == "":
            try_count += 1
            continue
        if is_stop(numb_inp):
            print("Ну и ладно :(")
            break
        try:
            if kind_of_numb == "int":
                res_n = int(numb_inp)
            if kind_of_numb == "float":
                res_n = float(numb_inp)
            is_error = False
        except Exception as err:
            # print(f"❌ err = {err}")
            is_error = True
        if is_error or (positive and not negative and res_n < 0) or \
                (not is_with_zero and res_n == 0):
            print(
                f"{'⚠️':>8} Нужно вводить {kind_adj_pl}"
                f"{(' ' + pos_or_neg_adj_pl) if pos_or_neg_adj_pl else ''}"
                f" числа.")
            numb_inp = ""
            res_n = None
            try_count += 1
            continue
    return res_n