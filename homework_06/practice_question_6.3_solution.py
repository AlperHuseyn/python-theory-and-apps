""" Instructor solutions for practice question #6.3 """

# 1st way: using list comprehension
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[x[i] for x in a] for i in range(len(a))]
print(transposed)

# 2nd way: using list comprehension (another way)
transposed = [[a[row][col] for row in range(len(a))] for col in range(len(a))]
print(transposed)

# 3rd way: using classical approach
result = []
for col in range(len(a)):
    temp = []
    for row in range(len(a)):
        temp.append(a[row][col])
    result.append(temp)
print(result)