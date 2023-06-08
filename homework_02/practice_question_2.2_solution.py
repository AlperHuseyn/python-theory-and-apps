""" Instructor solutions for practice question #2.2 """

val = int(input('Please enter an integer: '))

# 1st way: Using an empty list
digits = []
while val:
    # chr(ord('0') + single_digit_int_val) converts s_d_i_v into str
    digits.append(chr(ord('0') + val % 10))
    val //= 10

digits.reverse()
s = ''.join(digits)
print(s)

# 2nd way: an easier version, using an empty str
val = int(input('Please enter an integer: '))

s = ''
while val:
    s += chr(ord('0') + val % 10)
    val //= 10

s = s[::-1]
print(s)
