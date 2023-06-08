""" Instructor solution to practice question #6.2 """

lst = [1, 7, 2, 3, 4, 8, 5]
tlst = [(elem, ['even', 'odd'][elem % 2]) for elem in lst]
print(tlst)
