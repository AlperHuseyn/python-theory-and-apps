""" Instructor's solutions for n + nn + nnn + nnnn pattern """

n = int(input('Please type single digit int value: '))

# 1st way
rs = n + n * 11 + n * 111 + n * 1111
print(rs)

