""" Instructor solution for practice question #3.8 """


def print_shape(n):
    for i in range(n, 0, -1):
        print('*' * i + ' ' * (n - i) * 2 + '*' * i)
    for j in range(1, n + 1):
        print('*' * j + ' ' * (n - j) * 2 + '*' * j)


print_shape(10)