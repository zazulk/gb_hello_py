# Создать программный файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных будет
# свидетельствовать пустая строка.

# Вариант 2. Сразу в цикле дописываем в файл введенный пользователем текст

el = None
lines = []
ind = 1

while True:
    try:
        with open(f"file for task 1 v{ind}.txt", "x+", encoding="utf-8") \
                as result:
            # счетчик оборотов цикла
            count = 0
            while el != "":
                el = input("Вводите данные: ").strip()
                # если пользователь сразу вводит пустую строку, ругаемся
                if not count and el == "":
                    print("\t⚠️ Я так не играю! Отказываюсь создавать пустые "
                          "файлы.")
                    el = None
                    continue
                print(el, file=result)
                count += 1
            print("-" * 20)
            print(f"Записал в файл \"{result.name}\" вот такое:\n")
            result.seek(0)
            content = result.read()
            print(content)
        break
    except FileExistsError:
        ind += 1
        continue
    except IOError:
        print("❌ Произошла ошибка ввода-вывода")
        break
