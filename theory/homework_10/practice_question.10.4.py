""" My approach to practice question 10.4, get_file_size function """

import os


def get_file_size(path):
    f = open(path, 'r', encoding='utf-8')
    f.seek(0, 2)
    f_size = f.tell()
    f.close()
    return f_size


p = f'{os.getcwd()}' + r"\Nature's Fury- Surviving Storms and Volcanic Eruptions.txt"

print(f'File size: {get_file_size(p)}')
