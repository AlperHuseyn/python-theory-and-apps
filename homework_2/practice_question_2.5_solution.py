""" Instructor solution(s) for practice question #2.3 """

num = int(input('Please enter a number for the range: '))

for i in range(num + 1):
    k = i
    while k:
        if k % 2 != 0:
            break
        k //= 10
    else:
        print(i, end=' ')
