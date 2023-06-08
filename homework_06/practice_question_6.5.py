""" My approach to practice question #6.5 """
import itertools, statistics

a = [1, 2, 3, 4, 5]
clt = [statistics.mean(subset) for subset in itertools.combinations(a, 2)]
print(clt)
print(statistics.mean(clt), '\n', statistics.mean(a))
