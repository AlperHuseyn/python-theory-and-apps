""" My approach to practice question 10.2, disp_last_lines function """

import os


def disp_last_lines(path, number_of_lines):
    f = open(path, 'rb')
    f.seek(-number_of_lines, 2)
    print(f.read().decode('utf-8'), end='')
    f.close()


# Pycharm sets current working directory where the project is created,
# so getting the root path via os.getcwd() and adding file name to it works for me
p = f'{os.getcwd()}' + r"\Nature's Fury- Surviving Storms and Volcanic Eruptions.txt"
n_lines = 1024

disp_last_lines(p, n_lines)
