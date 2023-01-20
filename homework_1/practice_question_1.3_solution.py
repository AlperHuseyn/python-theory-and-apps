""" Instructor's solutions for n + nn + nnn + nnnn pattern """

"""
n = int(input('Please type single digit int value: '))

# 1st way:
rs = n + n * 11 + n * 111 + n * 1111
print(rs)
"""

# 2nd way: Using str typ casting and repitition
n = input('Please type single digit int value: ')
rs = int(n) + int(n * 2) + int(n * 3) + int(n * 4)
print(rs)
