# Сформировать (не программно) текстовый файл. В нём каждая строка должна
# описывать учебный предмет и наличие лекционных, практических и лабораторных
# занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести его на экран.

from itertools import filterfalse
from my_funcs import is_numb_str
from my_funcs import is_stop
from my_funcs import to_pretty_string
from my_funcs import is_senseless_line


def prepare_classes_with_sum_of_hours(file_name):
    def turn_into_numb(text):
        """Превращает строчное обозначение часов типа "N(лаб)" в число N.0
        float - на всякий случай, ведь может указываться не целое значение

        :param str text: строчное обозначение часов типа "N(лаб)"
        :return float:
        """
        res = text.strip().replace("(л)", "").replace("(пр)", "").replace(
            "(лаб)", "").replace(",", ".")
        return round(float(res)) if is_numb_str(res) else 0

    def get_sum_of_hours(text):
        """Считает сумму чисел, извлеченных из строки
        вида "Предмет: N(л) – N(лаб)"

        :param str text: Строка вида "Предмет: N(л) – N(лаб)".
        :return float: Сумма извлеченных чисел.
        """
        return sum([turn_into_numb(el) for el in text.split(":")[1].split()])

    success = False
    while not success:
        try:
            with open(file_name, "r") as file:
                lines = list(filterfalse(is_senseless_line, file.readlines()))
                classes = {line.split(":")[0].strip(): get_sum_of_hours(line)
                           for line in lines}
                print(to_pretty_string(classes))
                success = True
        except FileNotFoundError:
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
