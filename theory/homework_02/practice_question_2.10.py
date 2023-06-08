""" My approach to practice question #2.10 """

num = int(input('Please enter a number for num: '))

for i in range(-num, num + 1):
    if i < 0:
        print(' ' * (-i) + '*' * (2 * num + 1 + 2 * i))
    else:
        print(' ' * i + '*' * (2 * num + 1 - 2 * i))
