""" My approach to practice question #3.30c """


def bailey_borwein_plouffe_pi(k):
    pi = 0
    for n in range (k + 1):
        pi += (1 / 16) ** n * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))

    return pi


print(bailey_borwein_plouffe_pi(30))
