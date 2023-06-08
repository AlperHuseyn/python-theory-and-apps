""" Instructor solution(s) for practice question #2.3 """

n = int(input('Please enter a number for n: '))

umatrix = []

for idx in range(n):
    row = [0] * n
    row[idx] = 1
    umatrix.append(row)

print(umatrix)

# 1st way: Printing matrix using nested loops
for r in umatrix:
    for c in r:
        print(c, end=' ')
    print()

print()

# 2nd way: Printing matrix using nested loops
for r in range(n):
    for c in range(n):
        print(umatrix[r][c], end=' ')
    print()
