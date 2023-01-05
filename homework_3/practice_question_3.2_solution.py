""" Instructor solution(s) for practice question #3.2 """


def disp_shape(num):
    for i in range(num):
        print(' ' * i, end='')
        for j in range(i + 1, num + 1):
            print(j, end=' ')
        print()

    for i in range(num - 1, 0, -1):
        print(' ' * (i - 1), end='')
        for j in range(i, num + 1):
            print(j, end=' ')
        print()


disp_shape(5)
