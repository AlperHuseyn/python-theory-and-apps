""" My approach to practice question #6.3 """

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = []
for i in range(len(a[0])):
    transposed.append([row[i] for row in a])
print(transposed)
