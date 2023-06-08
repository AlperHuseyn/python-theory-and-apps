""" My approach to practice question #3.8 """


def print_shape(num):
    for i in range(num, 0, -1):
        for _ in range(i):
            print('*', sep='', end='')

        print(' ' * (num - i) * 2, end='')

        for _ in range(i, 0, -1):
            print('*', sep='', end='')

        print()

    for i in range(num, 0, -1):
        for _ in range(i, num + 1):
            print('*', sep='', end='')

        print(' ' * (i * 2 - 2), end='')

        for _ in range(num + 1, i, -1):
            print('*', sep='', end='')

        print()


print_shape(10)
