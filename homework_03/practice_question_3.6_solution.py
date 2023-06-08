""" Insrtuctors solution for practice question #3.6 """


def digitate(vals):
    result = []
    for val in vals:
        digits = []
        for digit in str(val):
            digits.append(int(digit))
        result.append(tuple(digits))
    return result

values = [23, 4, 765, 34589, 42]
print(digitate(values))
