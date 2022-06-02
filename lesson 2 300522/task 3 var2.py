# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить,
# к какому времени года относится месяц (зима, весна, лето, осень). Напишите
# решения через list и dict.

stop_words = ["q", "й", "стоп", "stop", "cnjg", "флюгегехаймен"]
stop = False
numb_inp = ''
valid_numbs = str(list(range(1, 13))).replace(",", "").replace("[", "").replace(
        "]", "").split()
seasons = {
    "зима": {
        12: 'декабрь',
        1: 'январь',
        2: 'февраль',
    },
    "лето": {
        6: 'июнь',
        7: 'июль',
        8: 'август',
    },
    "весна": {
        3: 'март',
        4: 'апрель',
        5: 'май',
    },
    "осень": {
        9: 'сентябрь',
        10: 'октябрь',
        11: 'декабрь',
    },
}

# Пытаем пользователя, чтобы ввел валидные данные
while numb_inp not in valid_numbs:
    numb_inp = input("Введите число от 1 до 12 или 'Q' для выхода: ").strip()
    if numb_inp in stop_words:
        print(f"{'':>5}Ну и ладно :(")
        stop = True
        break
    if numb_inp == "":
        continue
    if not numb_inp.isdigit():
        print(f"{'⚠️':>5} Это даже не число :(")
        continue
    if int(numb_inp) not in range(1, 13):
        print(f"{'⚠️':>5}️ {numb_inp} не входит в промежуток между 1 и 12.")

if not stop:
    numb_inp = int(numb_inp)
    month_name = ""
    season_name = ""

    for season in seasons:
        val = seasons.get(season)
        month_name = val.get(numb_inp)
        if month_name:
            season_name = season
            break

    if not month_name:
        print(f"Не нашел {numb_inp}-й месяц.")
    else:
        print(f"{numb_inp}-й месяц это {month_name}, {season_name}.")
