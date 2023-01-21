""" My approach to practice question #7.3 """
import math


class Circle:
    def __init__(self, *, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def disp(self):
        print(f'center: (<{self.center_x}>, <{self.center_y}>), radius: <{self.radius}>')

    def move(self, x_off, y_off):
        self.center_x += x_off
        self.center_y += y_off

    def is_inside(self, x, y):
        return self.radius >= math.sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)


c = Circle(center_x=10, center_y=12, radius=5)
c.disp()

c.move(-2, 4)
c.disp()

print('Inside' if c.is_inside(5, 7) else 'Not inside')
