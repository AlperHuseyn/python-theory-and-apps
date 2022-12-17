""" My approach to practice question #5 """

entered_txt = input('Please type the text which will be centered: ')
prnt_width = int(input('Please type the width: '))

if len(entered_txt) >= prnt_width:
    print(entered_txt)
else:
    spcs = prnt_width - len(entered_txt)
    splt = spcs // 2 + (spcs % 2)

    print(':', sep='', end='')  # for illustration purposes
    for _ in range(splt):
        print(' ', sep='', end='')
    print(entered_txt, end='')
    for _ in range(spcs-splt):
        print(' ', sep='', end='')
    print(':')  # for illustration   purposes
