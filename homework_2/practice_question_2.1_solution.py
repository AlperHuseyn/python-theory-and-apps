""" Instructor solutions for practice question #2.1 """

# 1st way: left to right multiply by 10, then add them together
nm_txt = input('Please type numerical text of type int: ').strip()

INPUT = 0
for ch in nm_txt:
    INPUT = INPUT * 10 + ord(ch) - ord('0')

print(INPUT * 2, type(INPUT))

# 2nd way: right to left multiply the digit by the power of 10
nm_txt = input('Please type numerical text of type int: ').strip()

INPUT = 0
DIGIT = 1
for ch in nm_txt[::-1]:
    INPUT += (ord(ch) - ord('0')) * DIGIT
    DIGIT *= 10

print(INPUT * 2, type(INPUT))
