""" My approach to practice question #4 """

nm_txt = input('Please type a numerical text of type int: ')
to_int = (ord(nm_txt[0]) - ord('0')) * 100 + (ord(nm_txt[1]) - ord('0')) * 10 + (ord(nm_txt[-1]) - ord('0'))
print(to_int, type(to_int))

