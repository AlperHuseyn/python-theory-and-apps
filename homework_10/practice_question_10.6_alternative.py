""" My approach tp practice question 10.6, read_csv function """

import os


def read_csv(path, sep=',', skip_rows=0, converter={}):
    data = []
    with open(path, 'r') as file:
        for _ in range(skip_rows):
            next(file)
        row = []
        in_quotes = False
        for line in file:
            if line.strip().startswith('"') and not in_quotes:
                in_quotes = True
            elif line.strip().endswith('"') and in_quotes:
                in_quotes = False
                line = line.strip()
                if len(line) > 1:
                    row.append(line[1:-1])
                data.append(row)
                row = []
                continue
            if in_quotes:
                row.append(line.strip())
            else:
                fields = line.strip().split(sep)
                for i, field in enumerate(fields):
                    field = field.strip('"').strip()
                    if len(converter) > 0 and i in converter:
                        field = converter[i](field)
                    row.append(field)
        if row:
            data.append(row)

    return data


cwd = os.getcwd()
p = f'{cwd}\\read.csv'
result = read_csv(p, sep=', ', skip_rows=1, converter={1: str, 2:str, 3: str})
print(result)
