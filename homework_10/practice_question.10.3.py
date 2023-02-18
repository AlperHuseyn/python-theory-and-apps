""" My approach to practice question 10.3, get_count function, lines, words, chars in a file """

import os

"""
def get_count(path):
    f = open(path, 'r', encoding='utf-8')
    f.seek(0, 2)  # set file pointer @ EOF
    f_size = f.tell()  # Get size in bytes (all line endings counted as a char)
    f.seek(0, 0)  # Set it back to beginning
    lines = f.readlines()
    words = 0
    for line in lines:
    
    f.close()

    return len(lines), words, f_size
"""


# Optimized version
def get_count(path):
    f = open(path, 'r', encoding='utf-8', newline=None)
    num_lines = 0
    num_words = 0
    num_chars = 0
    for line in f:
        num_lines += 1
        num_words += len(str(line).split())
        num_chars += len(line)

    f.close()

    return num_lines, num_words, num_chars


p = f'{os.getcwd()}' + r"\Nature's Fury- Surviving Storms and Volcanic Eruptions.txt"
number_of_lines, number_of_words, number_of_chars = get_count(p)
print(f'Number of lines: {number_of_lines}\nNumber of words: {number_of_words}\nNumber of chars: {number_of_chars}')
