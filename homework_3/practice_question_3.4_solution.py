""" Instructor solutions for practice question 3.4 """

import math


# 1st way: using math module log10 method
def is_armstrong(num):
    pw = int(math.log10(num)) + 1
    tmp = num
    total = 0
    while tmp:
        total += (tmp % 10) ** pw
        tmp //= 10

    return num == total


while True:
    val = int(input('Enter a value: '))
    if val == 0:
        break
    print('Armstrong' if is_armstrong(val) else 'Not Armstrong')


# 2nd way: str(num)
def is_armstrong(num):
    digits = str(num)
    total = 0
    for digit in digits:
        total += int(digit) ** len(digits)

    return num == total


while True:
    val = int(input('Enter a value: '))
    if val == 0:
        break
    print('Armstrong' if is_armstrong(val) else 'Not Armstrong')