import random
import os


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
    is_err, is_val_err = False, False

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
            print(f"\tТак, ладно, сам выберу. Выбрал {res_n}.")
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
            is_err = False
        except ValueError:
            is_val_err = True
        except Exception as err:
            is_err = True
        if is_err or is_val_err or (positive and not negative and res_n < 0)\
                or (not is_with_zero and res_n == 0):
            if is_err:
                print("\t❌ Что-то пошло очень не так...")
            else:
                print(
                    f"\t⚠️ Нужно вводить {kind_adj_pl}"
                    f"{(' ' + pos_or_neg_adj_pl) if pos_or_neg_adj_pl else ''}"
                    f" числа.")
            numb_inp = ""
            res_n = None
            try_count += 1
            continue
    return res_n


def has_punctuations(text):
    """Проверяет, что в переданной строке есть знаки пунктуации

    :param str text:
    :return bool:
    """
    if type(text) is not str:
        return False
    punctuations = [",", ".", "!", ":", "?", ";", "\\", "/", "(", ")",
                    "{", "}", "[", "]"]
    for letter in list(text):
        if letter in punctuations:
            return True
    return False


def has_letters(text):
    """Проверяет, что в переданной строке есть буквы

    :param str text: переданный текст
    :return bool:
    """
    if type(text) is not str:
        return False
    letters = list("abcdefghijklmnopqrstuwyxzабвгдеёжзийклмнопрстуфхцчэюяъь")
    for letter in list(text):
        if letter in letters:
            return True
    return False


def to_pretty_string(item, is_with_tab=True):
    tab = "\t" if is_with_tab else ""
    if type(item) is dict:
        return "".join([f"{tab}{key} : {value}\n" for key, value in item.items()])
    elif type(item) in [list, tuple, set]:
        return f"{tab}" + f"\n{tab}".join([str(el) for el in item])
    else:
        return item


def is_senseless_line(line):
    return type(line) is not str or line == "\n" or line.startswith("#")


def find_path_to_file(file_name):
    """Возвращает абсолютный путь к файлу
    Ищет не по всем файлам, а только в текущей и внешней директории

    :param str file_name: Имя файла с расширением.
    :return str:
    """
    if not file_name or type(file_name) is not str:
        return None
    cur_dir_path = os.getcwd()
    for address, dirs, files in os.walk(cur_dir_path):
        if files.count(file_name):
            file_path = os.path.join(address, file_name)
            return file_path
    # Если в глубине ничего не нашли, пойдем искать в директории выше
    outer_dir_path = os.path.dirname(cur_dir_path)
    for address, dirs, files in os.walk(outer_dir_path):
        if files.count(file_name):
            file_path = os.path.join(address, file_name)
            return file_path
    return None


def get_path_for_new_file(file_name):
    """Возвращает абсолютный путь к файлу, который нужно создать
    Если файл с переданным названием, существует, возвращает путь к нему

    :param str file_name: Имя файла для создания.
    :return str: Абсолютный путь к этому файлу.
    """
    if not file_name or type(file_name) is not str:
        return None
    existing = find_path_to_file(file_name)
    if existing:
        return existing
    # вычисляем расширение из переданного названия файла
    file_type = file_name.split(".")[-1] if file_name.count(".") else "txt"
    cur_dir_path = os.getcwd()
    for address, dirs, files in os.walk(cur_dir_path):
        if all([f.endswith(f".{file_type}") for f in files]) or not dirs:
            return os.path.join(address, file_name)
    return cur_dir_path
