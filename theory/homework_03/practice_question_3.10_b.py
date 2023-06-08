""" My approach to practice question #3.10b """


def somayaji_pi(n):
    pi = 0
    for i in range(3, 3 + 2 * n, 4):
        pi += (4 / (i ** 3 - i))
    for i in range(5, 3 + 2 * n, 4):
        pi -= (4 / (i ** 3 - i))

    return pi + 3


print(somayaji_pi(10))
