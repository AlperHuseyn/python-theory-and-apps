""" My approach to practice question #3.6 """


def digitate(values):
    result = []
    for val in values:
        digits = str(val)
        each_val = []
        for digit in digits:
            each_val.append(int(digit))
        result.append(tuple(each_val))
    return result


vals = [23, 4, 765, 34589, 42]
rst = digitate(vals)
print(rst)
