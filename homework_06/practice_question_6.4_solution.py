""" Instructor solution(s) for practice question #6.4 """

a = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
transposed = [[row[i] for row in a if i < len(row)] for i in range(max(map(len, a)))]
print(transposed)

transposed = [[row[i] for row in a if i < len(row)] for i in range(max(len(elem) for elem in a))]
print(transposed)