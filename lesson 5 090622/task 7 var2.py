# Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка будет содержать данные о фирме: название, форма
# собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000
# 5000. Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со
# значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000,
# “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый список сохранить в
# виде json-объекта в соответствующий файл.

# Вариант 2. С помощью comprehensions создаем словарь фирм

import json

file_name_mask = "file for task 7"

try:
    with open(file_name_mask + " source.txt", "r") as file, \
            open(file_name_mask + " result.txt", "w+") as file_res:
        res = []
        lines = file.readlines()
        # составляем словарь с названий фирм и их прибылью
        all_firms = {line.split()[0]: round(float(line.split()[2]) -
                                            float(line.split()[3]), 2)
                     for line in lines}
        res.append(all_firms)
        # собираем отдельно словарь фирм только с положительной прибылью
        positives = {key: value for key, value in all_firms.items() if
                     value > 0}
        average_profit = round(sum(positives.values()) / len(positives.keys()),
                               2) if positives else 0
        res.append({"average_profit": average_profit})

        # сохраняем итоговый список в виде JSON
        json.dump(res, file_res, indent=4)
        print(f"✅ Результат в виде JSON-объекта записан в файл \"{file_res.name}\"")
        print("Вывести вам его содержание?")
        has_to_show = input("\tВведите \"ДА\" или enter для завершения "
                            "программы: ")
        if has_to_show.lower() in ["да", "lf"]:
            file_res.seek(0)
            print(f"\nВот, что в файле \"{file_res.name}\":\n{file_res.read()}")
except FileNotFoundError:
    print(f"❌ Некоторые файлы \"{file_name_mask}\" не найдены.")
except IOError:
    print("❌ Произошла ошибка ввода-вывода")
except ValueError:
    print(f"❌ В некоторых файла \"{file_name_mask}\" содержатся "
          f"некорректные данные.")
