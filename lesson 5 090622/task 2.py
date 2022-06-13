# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# ⚠️ Пунктуацию и спец символы словами не считаем

from my_funcs import has_letters
from my_funcs import is_stop

file_name = "file for task 2.txt"
success = False

while not success:
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            print(f"\nОбщее количество строк в файле: {len(lines)}")
            lines = [line.split() for line in lines]
            for i, line in enumerate(lines, 1):
                # print(f"line {i} = \"{line}\"")
                words_count = len([w for w in line if has_letters(w)])
                print(f"\tколичество слов в строке {i}: {words_count}")
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