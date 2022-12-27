""" My approach to practice question #2.1 """

n = int(input('Please enter a number for n: '))

matrix = []
for idx in range(n):
    row = [0] * n
    matrix.append(row)
    for _ in row:
        row[idx] = 1


for row in matrix:
    print(row)


