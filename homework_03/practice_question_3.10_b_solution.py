""" Instructor solution for practice question #3.10b """


def somayaji_pi(n):
    total = 3
    for i in range(1, n + 1):
        total += (1 if i % 2 == 1 else -1) * (4 / ((2 * i + 1) ** 3 - (2 * i + 1)))

    return total


print(somayaji_pi(10))
