""" Using list comprehension for solving this question  """


def digitate(values):
    return [tuple([int(digit) for digit in str(val)]) for val in values]


vals = [23, 4, 765, 34589, 42]
rst = digitate(vals)
print(rst)