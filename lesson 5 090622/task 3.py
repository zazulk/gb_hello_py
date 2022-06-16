# Создать текстовый файл (не программно). Построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

from itertools import filterfalse
from my_funcs import is_stop
from my_funcs import is_senseless_line
from my_funcs import to_pretty_string
from my_funcs import find_path_to_file

file_name = "file for task 3.txt"
success = False

while not success:
    try:
        with open(find_path_to_file(file_name), "r", encoding="utf-8") as file:
            lines = list(filterfalse(is_senseless_line, file.readlines()))
            staff = {line.split()[0]: float(line.split()[1]) for line in lines}
            # print(staff)
            less_20 = {name: salary for name, salary in staff.items()
                       if salary < 20_000}
            print(f"У следующих сотрудников оклад менее 20 тысяч:")
            print(to_pretty_string(less_20))
            medium_salary = sum(staff.values()) / len(staff.keys())
            print(f"Средний доход: {medium_salary:.2f}")
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
        print(f"❌ В файле \"{file_name}\" содержатся некорректные данные.")
        break
