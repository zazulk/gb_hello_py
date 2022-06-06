# Реализовать функцию int_func(), принимающую слова из маленьких латинских
# букв и возвращающую их же, но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Нужно сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Используйте написанную ранее функцию
# int_func().

def int_func(token):
    """Принимает слова из маленьких латинских букв и возвращает их же,
    но с прописной первой буквой

    :param str token: Слово.
    :return str: Слово с прописной первой буквой.
    """
    if type(token) is not str:
        return ""
    return token.capitalize()


def capitalize_every_word(text):
    """Возвращает текст, сделав большой каждую первую букву в каждом слове.

    :param str text: текст
    :return str: измененный текст
    """
    if type(text) is not str:
        return ""
    return " ".join(map(int_func, text.split()))


def has_nonlatin_or_upper_symbs(text):
    """Проверяет, что в тексте есть не только маленькие латинские буквы

    :param str text: текст
    :return bool:
    """
    letters = list("abcdefghijklmnopqrstuwyxz")
    for char in text:
        if char not in letters and char != " ":
            return True
    return False


stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
inp = ""

print("Сделаю все слова в вашей фразе с большой буквы.")
while not inp:
    inp = input("Введите слова, состоящие из маленьких латинских букв, "
                "или 'Q' для выхода: ").strip()
    if inp in stop_words:
        print("Ну и ладно :(")
        stop = True
        break
    if has_nonlatin_or_upper_symbs(inp):
        print(
            f"{'⚠️':>8}Слова должны состоять исключительно из маленьких "
            f"латинских букв.")
        inp = ""
        continue

if not stop:
    print(f"🏁 Результат: {capitalize_every_word(inp)}")
