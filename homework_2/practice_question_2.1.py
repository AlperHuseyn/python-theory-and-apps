""" My approach to practice question #2.1 """

nm_txt = input('Please type numerical text of type int: ').strip()

to_int = 0
length = len(nm_txt)
for i in range(length):
    to_int += (ord(nm_txt[i]) - ord('0')) * 10 ** (length - 1)
    length -= 1

print(to_int * 2, type(to_int))
