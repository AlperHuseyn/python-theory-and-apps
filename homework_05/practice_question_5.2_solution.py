""" Instructor approach to practice question #5.2 """


def increasing_numbers(s):
    prev_val = -1
    position = 0
    result = []
    for i in range(1, len(s) + 1):
        val = int(s[position:i])
        if val > prev_val:
            result.append(val)
            prev_val = val
            position = i
    return result


r = increasing_numbers('3141592653589793238462643')  # [3, 14, 15, 92, 653, 5897, 9323, 84626]
print(r)