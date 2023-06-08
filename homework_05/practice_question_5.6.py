""" My approach to practice question #5.6 """

import random, statistics
import matplotlib.pyplot as plt

SAMPLE_SIZE = 5
NSAMPLES = 5000

population = list(range(10_000))

means = []

for _ in range(NSAMPLES):
    smeans = statistics.mean(random.sample(population, SAMPLE_SIZE))
    means.append(smeans)

plt.hist(means)
plt.show()
