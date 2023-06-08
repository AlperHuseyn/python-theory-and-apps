""" Instructor solution(s) for practice question #2.3 """

s = input('Please enter a text: ')

nl = 0
np = 0

for ch in s:
    if ch.isupper():
        np += 1
    elif ch.islower():
        nl += 1

print('Upper case letters number: {}'.format(np))
print('Lower case letters number: {}'.format(nl))
