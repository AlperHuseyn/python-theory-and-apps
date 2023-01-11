""" My approach to practice question # 5.7 """

import math
import matplotlib.pyplot as plt

def gaussian_pdf(x, mu=0, sigma=1):
    return (1.0 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-0.5 * ((x - mu) / sigma)**2)

x_list = [x/10 for x in range(-100,101)]
y_list = [gaussian_pdf(elem) for elem in x_list]
plt.plot(x_list, y_list)
plt.show()