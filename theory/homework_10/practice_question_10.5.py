""" My approach to practice question 10.5, copy_file """

import os

"""
def copy_file(path,  n_bytes):
    f = open(path, 'r', encoding='utf-8')
    read = f.read(n_bytes)
    idx = path.rfind('\\')
    path = path[idx + 1:]
    ext_idx = path.rfind('.')
    path = path[:ext_idx] + '_copy(1).txt'
    c = open(path, 'w', encoding='utf-8')
    c.write(read)
    c.close()
    f.close()
    return c
"""


def copy_file(source_path, destination_path):
    f = open(source_path, 'r', encoding='utf-8')
    read = f.read()
    f.close()
    c = open(destination_path, 'w', encoding='utf-8')
    c.write(read)
    c.close()
    return c


sp = f'{os.getcwd()}' + r"\Nature's Fury- Surviving Storms and Volcanic Eruptions.txt"
dp = f'{os.getcwd()}' + f"\\Nature's Fury- Surviving Storms and Volcanic Eruptions_copy.txt"
cf = copy_file(sp, dp)
