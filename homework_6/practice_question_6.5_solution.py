""" Instructor solutions for practice question #6.5 """

import itertools
import math
import statistics

# 1st way: using list comprehension
a = [1, 2, 3, 4, 5]
result = statistics.mean([statistics.mean(subset) for subset in itertools.combinations(a, 2)])
print(result)

# 2nd way: classical approach
total = 0
for subset in itertools.combinations(a, 2):
    total += statistics.mean(subset)

result = total / math.comb(len(a), 2)
print(result, '\n', statistics.mean(a))
