""" Instructor approach to practice question 9.1, time class"""


class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second
        self._tseconds = self._total_seconds()

    def __str__(self):
        return f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}'

    def __repr__(self):
        return f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}-{self._tseconds}'

    def _total_seconds(self):
        return self._hour * 60 * 60 + self._minute * 60 + self._second

    def _seconds_to_time(self, tseconds):
        self._hour = tseconds // 3600
        self._minute = tseconds % 3600 // 60
        self._second = tseconds % 3600 % 60
        self._tseconds = tseconds

    def __lt__(self, t):
        return self._tseconds < t._tseconds

    def __le__(self, t):
        return self._tseconds <= t._tseconds

    def __gt__(self, t):
        return self._tseconds > t._tseconds

    def __ge__(self, t):
        return self._tseconds >= t._tseconds

    def __eq__(self, t):
        return self._tseconds == t._tseconds

    def __ne__(self, t):
        return self._tseconds != t._tseconds

    def __add__(self, t):
        if isinstance(t, int):
            result = Time()
            result._seconds_to_time((self._tseconds + t) % 86400)
            return result
        if isinstance(t, Time):
            result = Time()
            result._seconds_to_time((self._tseconds + t._tseconds) % 86400)
            return result

        raise TypeError(f'Invalid type: {type(t)}')

    __radd__ = __add__

    def __sub__(self, t):
        if isinstance(t, int):
            result = Time()
            result._seconds_to_time((self._tseconds - t) % 86400)
            return result
        if isinstance(t, Time):
            result = Time()
            result._seconds_to_time((self._tseconds - t._tseconds) % 86400)
            return result

    __rsub__ = __sub__

    def __int__(self):
        return self._tseconds

    def __bool__(self):
        return self._tseconds != 0

    def __getitem__(self, index):
        if index == 0:
            return self._hour
        if index == 1:
            return self._minute
        if index == 2:
            return self._second

        raise ValueError('Invalid index')

    def __setitem__(self, index, value):
        if index == 0:
            self._hour = value
        elif index == 1:
            self._minute = value
        elif index == 2:
            self._second = value
        else:
            raise ValueError('Invalid index')

        self._tseconds = self._total_seconds()


t1 = Time(22, 10, 24)
result = t1 + 5700
print(result)

t2 = Time(5, 40, 34)
result = t1 + t2
print(result)

result = t1 - t2
print(result)

if t1 > t2:
    print('t1 > t2')
elif t1 < t2:
    print('t1 < t2')
elif t1 == t2:
    print('t1 == t2')

result = int(t1)
print(t1)

print('Non-zero' if t1 else 'Zero')

t1[0] = 23
print(t1)
