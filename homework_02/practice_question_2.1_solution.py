""" Instructor solutions for practice question #2.1 """

# 1st way: left to right multiply by 10, then add them together
nm_txt = input('Please type numerical text of type int: ').strip()

inpt = 0
for ch in nm_txt:
    inpt = inpt * 10 + ord(ch) - ord('0')

print(inpt * 2, type(inpt))

# 2nd way: right to left multiply the digit by the power of 10
nm_txt = input('Please type numerical text of type int: ').strip()

inpt = 0
digit = 1
for ch in nm_txt[::-1]:
    inpt += (ord(ch) - ord('0')) * digit
    digit *= 10

print(inpt * 2, type(inpt))
