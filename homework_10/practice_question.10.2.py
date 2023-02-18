""" My approach to practice question 10.2, disp_last_lines function """

import os


def disp_last_lines(path, number_of_lines):
    f = open(path, 'r', encoding='utf-8')
    f.seek(0, 2)  # seek @ EOF
    f_size = f.tell()  # Get size
    f.seek(max(f_size - 1024, 0))  # Set pos @ last n characters
    lines = f.readlines()
    for line in lines[-number_of_lines:]:
        print(line, end='')
    f.close()


# Pycharm sets current working directory where the project is created,
# so getting the root path via os.getcwd() and adding file name to it works for me
p = f'{os.getcwd()}' + r"\Nature's Fury- Surviving Storms and Volcanic Eruptions.txt"
n_lines = 3

disp_last_lines(p, n_lines)
