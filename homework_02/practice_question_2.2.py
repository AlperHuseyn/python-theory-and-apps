""" My approach to practice question #2.2 """

int_val = int(input('Please enter an integer: '))

dct = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

digits = []
while int_val:
    digits.append(dct[int_val % 10])
    int_val //= 10

digits.reverse()
to_str = ''.join(digits)
print(to_str, type(to_str))
