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
    latin_small_chars = 'qwertyuiopasdfghjklzxcvbnm'
    if type(token) is not str or set(token).difference(latin_small_chars):
        return ""
    return token.capitalize()


stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
inp = ""
result = ""

print("Сделаю все слова в вашей фразе с большой буквы.")
while not inp:
    inp = input("Введите слова, состоящие из маленьких латинских букв, "
                "или 'Q' для выхода: ").strip()
    if not inp:
        continue
    if inp in stop_words:
        print("Ну и ладно :(")
        stop = True
        break
    words = inp.split()
    for w in words:
        cap_w = int_func(w)
        if not cap_w:
            print(
                f"{'⚠️':>8} Слова должны состоять исключительно из маленьких "
                f"латинских букв.")
            inp = ""
            result = ""
            break
        else:
            result += f" {cap_w}"

if not stop:
    print(f"🏁 Результат: {result}")
