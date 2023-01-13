""" My approach to practice question #6.2 """

lst = [1, 7, 2, 3, 4, 8, 5]
tlst = [(elem, 'odd' if elem % 2 != 0 else 'even') for elem in lst]
print(tlst)