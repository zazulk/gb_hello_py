# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить,
# к какому времени года относится месяц (зима, весна, лето, осень). Напишите
# решения через list и dict.

numb_inp = 0
while numb_inp not in range(1, 13):
    numb_inp = int(input("Введите число от 1 до 12: "))
    if numb_inp not in range(1, 13):
        print(f"{numb_inp:>5} не входит в промежуток между 1 и 12.")

seasons = [
    {
        "name": "зима",
        "months": {
            12: "декабрь",
            1: "январь",
            2: "февраль"
        }
    },
    {
        "name": "лето",
        "months": {
            6: "июнь",
            7: "июль",
            8: "август"
        }
    },
    {
        "name": "весна",
        "months": {
            3: "март",
            4: "апрель",
            5: "май"
        }
    },
    {
        "name": "осень",
        "months": {
            9: "сентябрь",
            10: "октябрь",
            11: "декабрь"
        }
    },
]

month_name = ""
season_name = ""

for season in seasons:
    val = season.get("months")
    month_name = val.get(numb_inp)
    if month_name:
        season_name = season.get("name")
        break

print(f"{numb_inp}-й месяц это {month_name}, {season_name}.")
