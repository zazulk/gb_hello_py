# Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в
# файле и выводить её на экран.

from random import randrange
import os

file_name = "file for task 5.txt"

try:
    with open(file_name, "w+") as file:
        numbs = [str(randrange(1, 100)) for n in range(10)]
        file.write(" ".join(numbs))
        file.seek(0)
        content = file.read()
        print(f"Содержание файла \"{file.name}\":\n{content}")
        sum_num = sum([int(num) for num in content.split()])
        print(f"\nСумма всех чисел = {sum_num}")
        has_to_delete = input(f"\nУдалить файл \"{file.name}\"? Введите \"ДА\" "
                              "или enter для завершения программы: ")
        if has_to_delete.lower() in ["да", "lf"]:
            os.remove(file_name)
            print(f"🗑 Файл \"{file.name}\" удалён.")
except FileNotFoundError:
    print(f"❌ Файл \"{file_name}\" не найден.")
except IOError:
    print("❌ Произошла ошибка ввода-вывода")
except ValueError:
    print(f"❌ В файлe \"{file_name}\" содержатся некорректные данные.")
