""" Printing n + nn + nnn + nnnn pattern, my solution """

n = int(input('Please type single digit int value: '))
print(f'{n} + {n * 10 + n} + {n * 100 + n * 10 + n} + {n * 1000 + n * 100 + n * 10 + n}')
