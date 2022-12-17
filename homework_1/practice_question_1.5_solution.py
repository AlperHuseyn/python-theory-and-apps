# pylint: disable=C0103
""" Instructor solution fo practice question #5 """

# Using repetition
s = input('Please type the text which will be centered: ')
n = int(input('Please type the width: '))

ws_count = n - len(s)

o_put = ' ' * (ws_count // 2) + ' ' * (ws_count % 2) + s + ' ' * (ws_count // 2)
print(':' + o_put + ':')  # for illustration purposes
