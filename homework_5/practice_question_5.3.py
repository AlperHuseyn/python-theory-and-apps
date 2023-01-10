""" My approach to practice question #5.3"""


def consecutive_total(lst, n):
    if n > len(lst):
        return 'Error'

    largest_sum = 0
    index = 0
    for i in range(len(lst) - n + 1):
        current_sum = 0
        for j in range(i, i + n):
            current_sum += lst[j]
        if current_sum > largest_sum:
            largest_sum = current_sum
            index = i

    return largest_sum, index


print(consecutive_total([7, 77, 777], 2))
