# Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def get_user_info(name, surname, year, city, email, phone):
    """Возвращает словарь, заполненный передаваемой информацией о пользователя.

    Именованные параметры:
    name -- имя
    surname -- фамилия
    year -- год
    city -- город
    email -- email
    phone - моб телефон

    """
    res = {}
    if type(name) is str and name != "":
        res["имя"] = name
    if type(surname) is str and surname != "":
        res["фамилия"] = surname
    if type(year) is str and year != "":
        res["год рождения"] = year
    if type(city) is str and city != "":
        res["город"] = city
    if type(email) is str and email != "":
        res["email"] = email
    if type(phone) is str and phone != "":
        res["моб. телефон"] = phone
    return res


def has_empty_values(info):
    """Проверяет наличие не заполненных ключей в словаре.

    Если находит ключи с пустым значением, возвращает True,
    иначе — False.

    :param dict info: Словарь, ключи которого, надо проверить.
    :return bool:
    """
    for key in info:
        if not info.get(key):
            return True
    return False


def has_letters(text):
    """Проверяет, что в переданной строке есть буквы

    :param str text: переданный текст
    :return bool:
    """
    if type(text) is not str:
        # print("🎃🎃")
        return False
    letters = list("abcdefghijklmnopqrstuwyxzабвгдеёжзийклмнопрстуфхцчэюяъь")
    for letter in list(text):
        # print(f"🎃list(text) = {list(text)}")
        if letter in letters:
            # print("🎃")
            return True
    return False


def has_punctuations(text):
    """Проверяет, что в переданной строке есть знаки пунктуации

    :param str text:
    :return bool:
    """
    if type(text) is not str:
        # print("🧽🧽")
        return False
    punctuations = [",", ".", "!", ":", "?", ";", "\\", "/", "(", ")",
                    "{", "}", "[", "]"]
    for letter in list(text):
        # print(f"🧽list(text) = {list(text)}")
        if letter in punctuations:
            # print("🧽")
            return True
    return False


def normalize_year(year):
    """Приводит значение года к нормализованному виду.

    :param str year: Год.
    :return str:
    """
    if type(year) is not str:
        return ""
    res = year.replace("-", "").replace("года", "").replace(
        "год", "").replace("г", "").replace(".", "").replace(" ", "")
    if len(res) == 2:
        res = ("19" if int(res[:1]) > 22 else "20") + res
    if len(res) == 1:
        res = "200" + res
    return res


def remove_end_punctuations(text):
    """Удаляет пунктуацию в конце переданной строки

    :param str text:
    :return str:
    """
    if type(text) is not str:
        return ""
    punctuations = [",", ".", "!", ":", "?", ";", " "]
    while text[-1:] in punctuations:
        text = text[:-1]
    return text.strip()


def is_stop(text):
    """Проверяет, является ли текст стоп-словом

    :param str text:
    :return bool:
    """
    if type(text) is not str:
        return False
    stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
    return bool(text in stop_words)


stop = False
sample = {
    "имя": {
        "value": "",
        "normalizer": lambda val: val.title(),
        "validator": lambda val: len([s for s in val if s.isdigit()]) == 0 and
                                 len(val) > 1 and has_letters(val) and
                                 not has_punctuations(val),
        "err_msg": "Имя должно быть неоднобуквенным и не может содержать "
                   "цифры или пунктуацию. "
    },
    "фамилия": {
        "value": "",
        "normalizer": lambda val: val.title(),
        "validator": lambda val: len([s for s in val if s.isdigit()]) == 0 and
                                 has_letters(val) and not has_punctuations(val),
        "err_msg": "Фамилия должна быть неоднобуквенной и не может содержать "
                   "цифры или пунктуацию. "
    },
    "год рождения": {
        "value": "",
        "normalizer": normalize_year,
        "validator": lambda val: val.isdigit() and len(val) == 4,
        "err_msg": "Год рождения должен быть числом из 4 цифр."
    },
    "город": {
        "value": "",
        "normalizer": lambda val: val.title(),
        "validator": lambda val: len([s for s in val if s.isdigit()]) == 0 and
                                 has_letters(val) and not has_punctuations(val),
        # "validator": lambda val: any(.isdigit()]),
        "err_msg": "Название города не может содержать цифры или пунктуацию."
    },
    "email": {
        "value": "",
        "validator": lambda val: val.count("@") == 1 and
                                 val.index("@") not in [0, -1] and
                                 val.count(".") == 1 and
                                 val.index(".") > val.index("@"),
        "err_msg": "Email должен быть в формате user@hostname.domain"
    },
    "моб. телефон": {
        "value": "",
        "normalizer": lambda val: val.replace("+", "").replace("-", "").replace(
            "(", "").replace(")", "").replace(" ", "")[-10:],
        "validator": lambda val: val.isdigit() and len(val) in [10, 11],
        "err_msg": "Номер мобильного должен состоять из 10 цифр, не включая "
                   "первую 8 или 7."
    }
}
vals = []
inp = ''
i = 0
user_info = {}
for el in sample:
    user_info[el] = ""

user_params = user_info.keys()
# print(f"✏️ user_info = {user_info}")

# print(f"✏️️ user_params = {user_params}")

print("Вводите данные или 'Q' для выхода.")
while has_empty_values(user_info) and not stop:
    # print(f"🔹")
    # print(f"has_empty_values = {has_empty_values(user_info)}")
    for param in user_params:
        # print(f"🟢 {user_info[param]}")
        i += 1
        while not inp:
            # print("🔆")
            inp = remove_end_punctuations(input(f"{param:>8}: "))
            if "normalizer" in sample[param]:
                inp = sample[param].get("normalizer")(inp)
                # print(f"❕️ inp = {inp}")
                # print(f"❕️ {type(inp)}")
            if "validator" in sample[param]:
                is_valid = sample[param].get("validator")(inp)
                # print(f"❗️ is_valid = {is_valid}")
                # print(f"❗️has_letters = {has_letters(inp)}")
                # print(f"❗has_punctuations = {has_punctuations(inp)}")

                if not is_valid:
                    spec_msg = sample[param].get("err_msg")
                    print(
                        f"{'⚠️':>8} {spec_msg or 'Некорректные данные.'}")
                    inp = ''
        if is_stop(inp):
            print("Ну и ладно :(")
            stop = True
            break
        else:
            # print(f"💠inp = {inp}")
            vals.append(inp)
            inp = ''
    # print(f"❗️{vals}")
    if not stop:
        user_info = get_user_info(name=vals[0], surname=vals[1], year=vals[2],
                                  city=vals[3], email=vals[4], phone=vals[5])
    # print(f"❗❗️{user_info}")
    if i > 10:
        break

if not stop:
    print("." * 30)
    print("Вот, что у меня получилось:")
    for item in user_info:
        print(f"{item:>20}: {user_info.get(item)}")
    print("." * 30)
