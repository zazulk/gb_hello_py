# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма
# вновь введённых чисел будет добавляться к уже подсчитанной сумме. Но если
# вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.


def get_numbs_before_stop(tokens):
    """Возвращает токены из входящего списка токенов, стоящие до стоп-слова

    :param list tokens: токены
    :return list:
    """
    res = tokens.copy()
    for i in range(len(tokens)):
        if tokens[i] in stop_words:
            res = tokens[:i]
    return res


stop_words = ["q", "й"]
stop = False
res_sum = 0

print("Вводите числа, разделенные пробелом, а я буду все их суммировать, "
      "пока не напишите 'Q'.")

while not stop:
    inp_words = input("Введите строку чисел, разделённых пробелом: ").replace(
        ",", ".").split()
    try:
        inp_words_before_stop = get_numbs_before_stop(inp_words)
        stop = inp_words != inp_words_before_stop
        numbs = list(map(float, inp_words_before_stop))
        res_sum += sum(numbs)
        round_sum = round(res_sum, 3)
        if round_sum == res_sum:
            print(f"{'🏁' if stop else ''} Сумма = {res_sum}")
        else:
            print(f"{'🏁' if stop else ''} Сумма (округлил) = {round_sum}")

    except Exception:
        print("Для выхода нужно ввести 'Q'")
