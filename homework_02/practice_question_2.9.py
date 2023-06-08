""" My approach to practice question #2.9 """

height = int(input('Please enter the height of the pattern: '))
width = int(input('Please enter the width of the pattern: '))

direction = 1
position = 0

for _ in range(height):
    print('|' + ' ' * position + '*' + ' ' * (width - position - 1) + '|')
    if position == width - 1:
        direction = -1
    elif position == 0:
        direction = 1
    position += direction

