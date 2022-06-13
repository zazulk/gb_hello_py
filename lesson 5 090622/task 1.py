# Создать программный файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных будет
# свидетельствовать пустая строка.

el = None
lines = []
ind = 1

while el != "":
    el = input("Вводите данные: ").strip()
    if len(lines) == 0 and el == "":
        print("\t⚠️ Я так не играю! Отказываюсь создавать пустые файлы.")
        el = None
        continue
    lines.append(el + "\n")

while True:
    try:
        with open(f"file for task 1 v{ind}.txt", "x") as result:
            result.writelines(lines)
        break
    except FileExistsError:
        ind += 1
        continue
    except IOError:
        print("❌ Произошла ошибка ввода-вывода")
        break

try:
    with open(f"file for task 1 v{ind}.txt", "r") as new_file:
        print("-" * 20)
        print(f"Записал в файл \"{new_file.name}\" вот такое:\n")
        content = new_file.read()
        print(content)
except IOError:
    print("❌ Произошла ошибка ввода-вывода")
