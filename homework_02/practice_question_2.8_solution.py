""" Instructor solution(s) for practice question #2.8 """

a = [12, 56, 89, 32, 19, 99, 43]
print(a)

for i in range(len(a)):
    a[i] = a[i] % 10 * 10 + a[i] // 10

print(a)

