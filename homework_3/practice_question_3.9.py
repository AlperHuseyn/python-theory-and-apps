""" My approach to practice question #3.9 """


def disp_char_pattern(ch):
    char = ch.upper()

    for idx, c in enumerate(range(ord('A') - 0, ord(char) - 0 + 1)):
        print(' ' * (ord(char) - ord('A') - idx) + chr(c), end='')
        print(' ' * (idx * 2 - 1) + chr(c) if idx != 0 else '')
    for idx, c in enumerate(range(ord(char) - 0 - 1, ord('A') - 0 - 1, -1)):
        print(' ' * (idx + 1) + chr(c), end='')
        print(' ' * ((ord(chr(c)) - ord('A')) * 2 - 1) + chr(c) if idx != (ord(char) - ord('A') - 1) else '')


disp_char_pattern('k')
