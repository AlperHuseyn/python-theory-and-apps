""" Instructor's solution for the second practice question """

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101, 102, 103]

lst[:len(lst) // 2], lst[len(lst) // 2 + len(lst) % 2:] = lst[len(lst) // 2 + len(lst) % 2:], lst[:len(lst) // 2]
print(lst)
