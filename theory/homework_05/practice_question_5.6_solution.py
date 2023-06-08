""" Instructor solution for practice question #5.6 """

import random
import statistics
import matplotlib.pyplot as plt

SAMPLE_SIZE = 5
NSAMPLES = 5000

population = list(range(10000))
smeans = [statistics.mean(random.sample(population, SAMPLE_SIZE)) for _ in range(NSAMPLES)]

plt.hist(smeans)
plt.show()