""" My approach tp practice question 10.6, read_csv function """

import csv
import os


def read_csv(path, sep=',', skip_rows=0, converter={}):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=sep, quotechar='"')
        data = []
        for _ in range(skip_rows):
            next(csv_reader)
        for row in csv_reader:
            row_data = []
            for i, field in enumerate(row):
                if i in converter:
                    field = converter[i](field)
                row_data.append(field)
            data.append(row_data)

    return data


cwd = os.getcwd()
p = f'{cwd}\\read.csv'
result = read_csv(p, sep=',', skip_rows=1)
print(result)
