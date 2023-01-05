""" Instructor solution to practice question #3.9 """


def disp_char_patten(char):
    n = ord(char.upper()) - ord('A')
    print(' ' * n + 'A')
    for i in range(1, n + 1):
        print(' ' * (n - i) + chr(ord('A') + i) + ' ' * (2 * i - 1) + chr(ord('A') + i))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + chr(ord('A') + i) + ' ' * (2 * i - 1) + chr(ord('A') + i))
    print(' ' * n + 'A')


disp_char_patten('h')