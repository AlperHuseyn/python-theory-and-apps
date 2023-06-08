""" Swap list's elements """

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101, 102]
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101, 102, 103]

if len(lst) % 2 == 0:
    lst[:(len(lst) // 2) + 1], lst[(len(lst) // 2) + 1:] = lst[(len(lst) // 2):], lst[:len(lst) // 2]
else:
    lst[:(len(lst) // 2)], lst[(len(lst) // 2) + 1:] = lst[(len(lst) // 2) + 1:], lst[:len(lst) // 2]

print(lst)

