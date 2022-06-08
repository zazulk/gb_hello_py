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
