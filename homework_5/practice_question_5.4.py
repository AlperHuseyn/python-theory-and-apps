""" My approach to practice question #5.4 """


def move_machine(text):
    commands = text.split(';')
    case_ignored = list(map(str.upper, commands))
    x = 0
    y = 0
    for cmd in case_ignored:
        if cmd.split()[0] == 'UP':
            y += int(cmd.split()[1])
        elif cmd.split()[0] == 'RIGHT':
            x += int(cmd.split()[1])
        elif cmd.split()[0] == 'DOWN':
            y -= int(cmd.split()[1])
        else:
            x -= int(cmd.split()[1])

    return x, y


s = 'Up 4 ; Down 2 ; Down 3; Left 4; Up 2'
x, y = move_machine(s)

print((x, y))
