""" My approach to the practice question #2.5 """

num = int(input('Please enter a number for the range: '))

for i in range(num + 1):
    num_digits = len(str(i))
    for digit in str(i):
        if int(digit) % 2 == 0:
            num_digits -= 1
            if not num_digits:
                print(i, end=' ')
        else:
            break
