""" My approach to practice question 10.1, my_grep function """

import os


def my_grep(path, text):
    f = open(path, 'r', encoding='utf8')
    not_found = True
    for line_no, line in enumerate(f, 1):
        if text in line:
            print(f'{line_no:02d}: {line}', end='')
            not_found = False

    if not_found:
        print(f'File does not contain the word: "{text}"')


f = f'{os.getcwd()}' + r"\Nature's Fury- Surviving Storms and Volcanic Eruptions.md"
t = 'weather'  # text contains 5

my_grep(f, t)
