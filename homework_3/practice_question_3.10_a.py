""" My approach to practice question #3.10a """


import math


def newton_pi(k):
    sm = 0
    for n in range(k + 1):
        sm += (((2 ** (n + 1)) * (math.factorial(n) ** 2)) / math.factorial(2 * n + 1))

    return sm


print(newton_pi(50))
