""" Instructor solution for practice question #5.3 """


def consecutive_total(a, n):
    max_val = sum(a[0:n])
    index = 0
    for i in range(1, len(a) + 1 - n):
        total = sum(a[i:i + n])
        if total > max_val:
            max_val = total
            index = i

    return max_val, index


a = [1, -2, 3, -4, -5, 6]
result = consecutive_total(a, 2)
print(result)
