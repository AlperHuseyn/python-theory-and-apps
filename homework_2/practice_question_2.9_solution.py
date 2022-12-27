""" Instructor solution for practice question 2.9 """

height = input('Please enter the pattern height: ')
width = input('Please enter the pattern width: ')

direction = 1
pos = 0

for _ in range(height):
    print('|' + ' ' * pos + '*' + ' ' * (width - pos - 1) + '|')
    if pos == width - 1:
        direction = -1
    elif pos == 0:
        direction = 1
    pos += direction
