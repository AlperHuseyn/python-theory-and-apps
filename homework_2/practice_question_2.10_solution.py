""" Instructor solution(s) for practice question #2.10 """

num = int(input('Please enter a number for num: '))

# 1st way: Loop start value '0'
for i in range(num):
    print(' ' * (num - i - 1) + '*' * (2 * i + 1))


for i in range(num - 2, -1, -1):
    print(' ' * (num - i - 1) + '*' * (2 * i + 1))

# 1st way: Loop start value '1'
num = int(input('Please enter a number for num: '))

for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * (2 * i - 1))


for i in range(num - 1, -1, -1):
    print(' ' * (num - i) + '*' * (2 * i - 1))
