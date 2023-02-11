""" My approach to practice question 9.1, time class"""


class Time(object):

    SECONDS_IN_AN_HOUR = 3600
    SECONDS_IN_A_MINUTE = 60
    SECONDS_IN_A_DAY = 86400

    def __init__(self, hour=0, minute=0, second=0):
        self.t_seconds = None
        self.hour = hour
        self.minute = minute
        self.second = second
        self._total_seconds()

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}-{self.t_seconds:05d}'

    def _total_seconds(self):
        total = 0
        for i in range(self.hour):
            total += Time.SECONDS_IN_AN_HOUR

        for i in range(self.minute):
            total += Time.SECONDS_IN_A_MINUTE

        total += self.second
        self.t_seconds = total

    def seconds_to_time(self, t_seconds):
        total = 0
        i = 0
        while True:
            if total + Time.SECONDS_IN_AN_HOUR >= t_seconds:
                break
            total += Time.SECONDS_IN_AN_HOUR
            i += 1

        self.hour = i

        i = 0
        while True:
            if total + Time.SECONDS_IN_A_MINUTE >= t_seconds:
                break
            total += Time.SECONDS_IN_A_MINUTE
            i += 1

        self.minute = i
        second = t_seconds - total

        self.second = second
        self.t_seconds = t_seconds

    def __lt__(self, other):
        return other.t_seconds > self.t_seconds

    def __le__(self, other):
        return other.t_seconds >= self.t_seconds

    def __gt__(self, other):
        return other.t_seconds < self.t_seconds

    def __ge__(self, other):
        return other.t_seconds <= self.t_seconds

    def __eq__(self, other):
        return self.t_seconds == other.t_seconds

    def __ne__(self, other):
        return other.t_seconds != self.t_seconds

    def __add__(self, other):
        if isinstance(other, int):
            added = self.t_seconds + other
        elif isinstance(other, Time):
            added = self.t_seconds + other.t_seconds
            if added >= Time.SECONDS_IN_A_DAY:
                added -= Time.SECONDS_IN_A_DAY
        else:
            raise TypeError(f'Invalid type parameter: {type(other)}')

        t = Time()
        t.seconds_to_time(added % Time.SECONDS_IN_A_DAY)

        """
        t.seconds_to_time(added)
        
        if t.hour >= 24:
            t.hour -= 24
        if t.minute >= 60:
            t.minute -= 60
        if t.second >= 60:
            t.second -= 60
        """

        return t

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int):
            dif = self.t_seconds - other
        elif isinstance(other, Time):
            dif = self.t_seconds - other.t_seconds
        else:
            raise TypeError(f'Invalid type parameter: {type(other)}')

        if dif < 0:
            dif += Time.SECONDS_IN_A_DAY

        t = Time()
        t.seconds_to_time(dif)

        return t

    __rsub__ = __sub__

    def __int__(self):
        return int(self.t_seconds)

    def __bool__(self):
        return True if (self.t_seconds != 0 and self.minute != 0 and self.hour != 0) else False

    def __getitem__(self, idx):
        if idx < 0 or idx > 2:
            raise IndexError(f'Index out of range: {idx}')
        if idx == 0:
            return self.hour
        if idx == 1:
            return self.minute
        if idx == 2:
            return self.second

    def __setitem__(self, idx, value):
        if idx < 0 or idx > 2:
            raise IndexError(f'Index out of range: {idx}')
        if idx == 0:
            self.hour = value
        elif idx == 1:
            self.minute = value
        elif idx == 2:
            self.second = value


# Test 1: Test __str__ method
t1 = Time(22, 10, 24)
print(f't1: {t1}')

# Test 2: Test __repr__ method
print(f'repr: {repr(t1)}')

# Test 3: Test addition with int
print(f't1 + 5700: {5700 + t1}')

# Test 4: Test addition with Time
t2 = Time(5, 40, 34)
print(f't1 + t2: {t1 + t2}')

# Test 5: Test subtraction with Time
result = t2 - t1
print(f't2 - t1: {result}')

# Test 6: Test comparison with <
if t1 < t2:
    print('t1 < t2')

# Test 7: Test comparison with >
if t1 > t2:
    print('t1 > t2')

# Test 8: Test comparison with ==
if t1 == t2:
    print('t1 == t2')

# Test 9: Test comparison with <=
if t1 <= t2:
    print('t1 <= t2')

# Test 10: Test comparison with >=
if t1 >= t2:
    print('t1 >= t2')

# Test 11: Test comparison with !=
if t1 != t2:
    print('t1 != t2')

# Test 12: Test __int__ method
print(f'Passed seconds from "00:00:00" (t1): {int(t1)}')

# Test 13: Test __bool__ method
t3 = Time()
print(f'__bool__: {bool(t3)}')

# Test 14: Test __getitem__ method
print(f'Getting hour info (t2): {t2[0]}')
print(f'Getting second info (t2): {t2[2]}')

# Test 15: Test __setitem__ method
t2[0] = 23
print(f'Printing t2 after setting its hour: {t2}')
t2[2] = 56
print(f'Printing t2 after setting its second: {t2}')
