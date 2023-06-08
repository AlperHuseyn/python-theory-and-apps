"""
Alternative way to solve the first practice question
using reversed built-in function
"""

l1 = ['Alper', 10, 'ali', 'veli', 20, 'selami']
l2 = ['selami', 20, 'veli', 'ali', 10, 'Alper']

if list(reversed(l1)) == l2:  # reversed built-in function used instead of reverse method for not losing l1
    print('True')
else:
    print('False')
