""" Instructor solution for practice question # 5.7 """

import math
import matplotlib.pyplot as plt

x_list = [i * .1 for i in range(-100, 100)]
y_list = [(1 / 2 * math.pi) * math.e ** (-.5 * x ** 2) for x in x_list]
plt.plot(x_list, y_list)
plt.show()