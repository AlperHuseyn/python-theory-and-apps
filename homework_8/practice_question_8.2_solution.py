""" Instructor approach to practice question #8.2, Date class """


class Date(object):
    # list of integers representing the number of days in each month (starting with January) in a non-leap year.
    _mon_tab = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # list of integers representing the number of days in each month (starting with January) in a non-leap year.
    _day_text = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    def __init__(self, day, month=None, year=None):
        if month is None and year is None:
            if isinstance(day, int):
                self._convert_date(day)
            elif isinstance(day, str):
                self.day, self.month, self.year = [int(x) for x in day.split('/')]
                self._total_days()
            else:
                raise TypeError(f'Invalid type parameter: {type(day)}')
        else:
            self.day = day
            self.month = month
            self.year = year
            self._total_days()

    def __repr__(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year:04d}-{Date._day_text[self.t_days % 7]}-{self.t_days}'

    def __str__(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year:04d}-{Date._day_text[self.t_days % 7]}'

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def _total_days(self):
        total = 0
        for i in range(1900, self.year):
            total += 366 if Date.is_leap(i) else 365

        Date._mon_tab[1] = 29 if Date.is_leap(self.year) else 28

        for i in range(self.month - 1):
            total += Date._mon_tab[i]

        total += self.day
        self.t_days = total

    def _convert_date(self, t_days):
        total = 0
        i = 1900
        while True:
            doy = 366 if Date.is_leap(i) else 365
            if total + doy >= t_days:
                break
            total += doy
            i += 1

        self.year = i

        i = 0
        while True:
            if total + self._mon_tab[i] >= t_days:
                break
            total += self._mon_tab[i]
            i += 1

        self.month = i + 1
        self.day = t_days - total

        self.t_days = t_days

    def get_day_text(self):
        return Date._day_text[self.t_days % 7]

    def __lt__(self, dt):
        return dt.t_days < self.t_days

    def __le__(self, dt):
        return dt.t_days <= self.t_days

    def __gt__(self, dt):
        return dt.t_days > self.t_days

    def __ge__(self, dt):
        return dt.t_days >= self.t_days

    def __eq__(self, dt):
        return dt.t_days == self.t_days

    def __ne__(self, dt):
        return dt.t_days != self.t_days

    def compare(self, date):
        """
         takes in another date object and returns
          1 if the current object's date is greater,
         -1 if the current object's date is smaller, and
          0 if the dates are equal.
        """
        if self.t_days > date.t_days:
            return 1
        elif self.t_days < date.t_days:
            return -1
        return 0

    def __add__(self, day):
        return Date(self.t_days + day)

    __radd__ = __add__

    def __sub__(self, day):
        return Date(self.t_days - day)

    __rsub__ = __sub__

d = Date(37320)
k = Date('12/11/1992')
m = Date(10, 12, 2022)

print(d)
print(k)
print(m)

result = m + 2
print(result)

result = k - 2
print(result)
result = 4 - k
print(result)

if k > m:
    print('k > m')
elif k < m:
    print('k < m')
elif k == m:
    print('k == m')

print(m == d)
print(m != d)
print(m <= d)
print(m >= d)
print(m < d)
print(m > d)