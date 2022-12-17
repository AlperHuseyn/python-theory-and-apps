""" Instructor solution for practice question #4 """

# 1st way: Using dictionary
dct = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

nm_txt = input('Please type a numerical text of type int: ')

to_int = dct[nm_txt[0]] * 100 + dct[nm_txt[1]] * 10 + dct[nm_txt[2]]
print(to_int, type(to_int))

# 2nd way: Using int(...) built-in function
nm_txt = int(input('Please type a numerical text of type int: '))
print(to_int, type(to_int))


