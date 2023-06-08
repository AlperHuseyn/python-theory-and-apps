""" My approach to practice question #5.5 """

import random
import statistics

look_up = [0] * 10

for _ in range(5000):
    population = range(0, 10_000)
    sample = random.sample(population, 5)
    m = statistics.mean(sample)
    m = round(m)
    if m < 1000:
        look_up[0] += 1
    elif m in range(1000, 2000):
        look_up[1] += 1
    elif m in range(2000, 3000):
        look_up[2] += 1
    elif m in range(3000, 4000):
        look_up[3] += 1
    elif m in range(4000, 5000):
        look_up[4] += 1
    elif m in range(5000, 6000):
        look_up[5] += 1
    elif m in range(6000, 7000):
        look_up[6] += 1
    elif m in range(7000, 8000):
        look_up[7] += 1
    elif m in range(8000, 9000):
        look_up[8] += 1
    else:
        look_up[9] += 1

for elem in look_up:
    print('*' * (elem // 30), end='')
    print()
