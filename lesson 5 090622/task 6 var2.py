# Сформировать (не программно) текстовый файл. В нём каждая строка должна
# описывать учебный предмет и наличие лекционных, практических и лабораторных
# занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести его на экран.

# Вариант 2. С применением подсмотренного на разборе приема выделения чисел из
# строки с помощью comprehensions

from itertools import filterfalse
from my_funcs import is_stop
from my_funcs import to_pretty_string
from my_funcs import is_senseless_line
from my_funcs import find_path_to_file


def prepare_classes_with_sum_of_hours(file_name):
    success = False
    while not success:
        try:
            with open(find_path_to_file(file_name), "r", encoding="utf-8") \
                    as file:
                lines = list(filterfalse(is_senseless_line, file.readlines()))
                classes = {}
                for line in lines:
                    name, stats = line.split(':')
                    stats_sum = sum(map(int, "".join([i for i in stats if
                                        i == ' ' or '9' >= i >= '0']).split()))
                    classes[name] = round(stats_sum, 2)
                print(to_pretty_string(classes))
                success = True
        except FileNotFoundError or TypeError:
            print(f"❌ Файл \"{file_name}\" не найден.")
            file_name = input(f"\tВведите корректное имя файла или 'Q' для"
                              f" завершения программы: ").strip()
            if is_stop(file_name):
                break
            if not file_name.endswith(".txt"):
                file_name += ".txt"
        except IOError:
            print("❌ Произошла ошибка ввода-вывода")
            break
        except ValueError:
            print(f"❌ В файлe \"{file_name}\" содержатся некорректные данные.")
            break


prepare_classes_with_sum_of_hours("file for task 6.txt")
