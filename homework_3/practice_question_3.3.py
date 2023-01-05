""" My approach to practice question #3.3 """


def crown(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end='')

        for _ in range(num - i):
            print('  ', end='')

        for k in range(i, 0, -1):
            print(k, end='')

        for p in range(i - 1):
            print(p + 2, end='')

        for _ in range(num - i):
            print('  ', end='')

        for r in range(i, 0, -1):
            print(r, end='')
        print()


val = int(input('Enter a value: '))
crown(val)
