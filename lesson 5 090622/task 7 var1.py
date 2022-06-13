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

# Вариант 1. С помощью цикла по строкам файла создаем словарь фирм

import json

file_name_mask = "file for task 7"
enc = "utf-8"

try:
    with open(file_name_mask + " source.txt", "r", encoding=enc) as file, \
            open(file_name_mask + " result.txt", "w+", encoding=enc) as file_res:
        all_firms = {}
        pos_profits = []
        # составляем словарь с названий фирм и их прибылью
        for line in file:
            line_elems = line.split()
            profit = float(line_elems[2]) - float(line_elems[3])
            if profit > 0:
                pos_profits.append(profit)
            all_firms[line_elems[0]] = round(profit, 2)

        # вычисляем среднюю прибыль
        average_profit = round(sum(pos_profits) / len(pos_profits), 2) \
            if pos_profits else 0
        # собираем итоговый список и записываем его в файл в виде JSON
        res = [all_firms, {"average_profit": average_profit}]
        json.dump(res, file_res, indent=4)
        print(f"✅ Результат в виде JSON-объекта записан в файл "
              f"\"{file_res.name}\"")
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
