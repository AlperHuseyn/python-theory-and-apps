""" Instructor solution for practice question #5.5 """

import random
import statistics

SAMPLE_SIZE = 5
NSAMPLES = 5000

population = list(range(10_000))

counters = [0] * 10

for _ in range(NSAMPLES):
    smean = statistics.mean(random.sample(population, SAMPLE_SIZE))
    counters[int(smean / 1000)] += 1

for counter in counters:
    print('X' * round(counter / 50))
