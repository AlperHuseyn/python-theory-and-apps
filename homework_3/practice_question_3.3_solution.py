""" Instructor solution for practice question #3.3 """


# 1st way: for loop
def crown(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end='')

        print(' ' * (num - i) * 2, end='')

        for k in range(i, 0, -1):
            print(k, end='')

        for p in range(2, i + 1):
            print(p, end='')

        print(' ' * (num - i) * 2, end='')

        for r in range(i, 0, -1):
            print(r, end='')
        print()


crown(6)


# 2nd way: using asterisk
def crown(num):
    for i in range(1, num + 1):
        print(*range(1, i + 1), sep='', end='')
        print(' ' * (num - i) * 2, end='')
        print(*range(i, 0, -1), sep='', end='')
        print(*range(2, i + 1), sep='', end='')
        print(' ' * (num - i) * 2, end='')
        print(*range(i, 0, -1), sep='', end='')
        print()


crown(8)
