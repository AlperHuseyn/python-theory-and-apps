""" My approach to practice question #6.4 """

a = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
transposed = []
max_col = max(len(row) for row in a)
for i in range(max_col):
    temp = []
    for row in a:
        if i < len(row):
            temp.append(row[i])
    transposed.append(temp)
print(transposed)
