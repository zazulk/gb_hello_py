# Создать (не программно) текстовый файл. Напишите программу, открывающую
# файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# Вариант 2. Записываем в файл с помощью print
from my_funcs import find_path_to_file
from my_funcs import get_path_for_new_file
import os


def get_rus_numb(numb_name):
    """Возвращает соответствующее переданному название числа на русском языке

    :param str numb_name: Название числа.
    :return str: Перевод названия числа.
    """
    # Если передали фигню, вернем ее взад
    if type(numb_name) is not str:
        return numb_name
    eng_to_rus_numbs = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре"
    }
    result = eng_to_rus_numbs.get(numb_name.lower()) or numb_name
    return result if numb_name[0].islower() else result.capitalize()


def replace_eng_numb_with_rus(text):
    """Возвращает переданный текст, изменив название чисел на английском
    на названия этих чисел на русском

    :param str text: Переданная строка.
    :return str: Измененная строка.
    """
    # Если передали фигню, вернем ее взад
    if type(text) is not str:
        return text
    words = list(map(get_rus_numb, text.split()))
    # print(f"words = {words}")
    return " ".join(words)


file_name_mask = "file for task 4"
enc = "utf-8"
try:
    source_file = find_path_to_file(file_name_mask + " source.txt")
    result_file = get_path_for_new_file(file_name_mask + " result.txt")
    with open(source_file, "r", encoding=enc) as file, \
            open(result_file, "w+", encoding=enc) as res_file:
        for line in file:
            line_with_rus_numb = replace_eng_numb_with_rus(line)
            print(line_with_rus_numb, file=res_file)
        res_file.seek(0)
        content = res_file.read()
        print(f"Содержание итогового файла \"{os.path.basename(res_file.name)}"
              f"\":")
        print(content)
except FileNotFoundError:
    print(f"❌ Некоторые файлы \"{file_name_mask}\" не найдены.")
except IOError:
    print("❌ Произошла ошибка ввода-вывода")
except ValueError:
    print(f"❌ В некоторых файла \"{file_name_mask}\" содержатся "
          f"некорректные данные.")
