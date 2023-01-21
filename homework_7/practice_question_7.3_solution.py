""" Instructor solution for practice question #7.3 """
import math

class Circle:
    def __init__(self, centerx, centery, radius):
        self.centerx = centerx
        self.centery = centery
        self.radius = radius

    def disp(self):
        print(f'center: ({self.centerx}, {self.centery}), radius: {self.radius}')

    def move(self, xoff, yoff):
        self.centerx += xoff
        self.centery += yoff

    def isinside(self, x, y):
        return math.sqrt((self.centerx - x) ** 2 + (self.centery - y) ** 2) < self.radius


c = Circle(10, 12, 5)
c.disp()

c.move(-2, 4)
c.disp()

print('Inside' if c.isinside(5, 7) else 'Not inside')


