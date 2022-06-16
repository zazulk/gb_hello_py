# Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в
# файле и выводить её на экран.

from random import randrange
import os
from my_funcs import get_path_for_new_file

file_name = "file for task 5.txt"

try:
    with open(get_path_for_new_file(file_name), "w+", encoding="utf-8") as file:
        numbs = [str(randrange(1, 100)) for n in range(10)]
        file.write(" ".join(numbs))
        file.seek(0)
        content = file.read()
        file_basename = os.path.basename(file.name)
        print(f"Содержание файла \"{file_basename}\":\n{content}")
        sum_num = sum([int(num) for num in content.split()])
        print(f"\nСумма всех чисел = {sum_num}")
        has_to_delete = input(f"\nУдалить файл \"{file_basename}\"? Введите "
                              f"\"ДА\" или enter для завершения программы: ")
        if has_to_delete.lower() in ["да", "lf"]:
            os.remove(file.name)
            print(f"🗑 Файл \"{file_basename}\" удалён.")
except FileNotFoundError or TypeError:
    print(f"❌ Файл \"{file_name}\" не найден.")
except IOError:
    print("❌ Произошла ошибка ввода-вывода")
except ValueError:
    print(f"❌ В файлe \"{file_name}\" содержатся некорректные данные.")
