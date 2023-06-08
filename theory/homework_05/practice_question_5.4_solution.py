""" Instructor solution for practice question #5.4 """


def move_machine(text):
    x = y = 0
    cmds = text.split(';')
    for cmd in cmds:
        direction, val = cmd.split()
        direction = direction.lower()
        val = int(val)
        if direction == 'up':
            y += val
        elif direction == 'down':
            y -= val
        elif direction == 'right':
            x += val
        elif direction == 'left':
            x -= val
        else:
            raise ValueError('Invalid direction')

    return x, y


s = 'Up     4    ; Down 2 ; Down 3;     Left 4; Up 2'
x, y = move_machine(s)

print((x, y))

