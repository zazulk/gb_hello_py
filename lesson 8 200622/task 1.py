from random import randint


class DateException(Exception):
    def __init__(self, msg=None, valids=None, date_val=None):
        self.msg = msg
        self.is_valid_day, self.is_valid_month, self.is_valid_year = valids
        self.date_val = date_val
        if msg and not valids:
            super().__init__(f"⛔️ {msg}")

    def __str__(self):
        bad_value_of = f"⛔ {self.date_val or ''} Некорректное значение"
        bad_values = []
        if not self.is_valid_day:
            bad_values.append("дня")
        if not self.is_valid_month:
            bad_values.append("месяца")
        if not self.is_valid_year:
            bad_values.append("года")
        return bad_value_of + " " + ", ".join(bad_values)


class Date:
    def __init__(self, date_parts):
        self.day, self.month, self.year = date_parts

    @staticmethod
    def validate_date(date_parts):
        day, month, year = date_parts
        is_valid_year = 1 <= year <= 9999
        is_leap_year = year % 4 == 0
        is_valid_month = month <= 12
        is_valid_feb_day = month == 2 and (day <= 29 if is_leap_year else
                                           day <= 28)
        is_valid_day = day > 0 and (is_valid_feb_day or
                       (day <= 30 and month in [4, 6, 9, 11] or day <= 31 and
                        month not in [2, 4, 6, 9, 11]))
        return [is_valid_day, is_valid_month, is_valid_year]

    @classmethod
    def from_str(cls, date):
        date_numbs = [int(d) for d in date.split("-")]
        validations = cls.validate_date(date_numbs)
        if all(validations):
            return cls(date_numbs)
        else:
            raise DateException(valids=validations, date_val=date)

    def __str__(self):
        return f"day: {self.day}, month: {self.month}, year: {self.year}"


valid_count = 0
while valid_count < 8:
    try:
        lst = [str(randint(0, 3)) + str(randint(0, 9)), str(randint(0, 2)) +
               str(randint(0, 3)), str(randint(0, 10001))]
        new_date = Date.from_str("-".join(lst))
        print(new_date)
        valid_count += 1
    except Exception as err:
        print(err)
