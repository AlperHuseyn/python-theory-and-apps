""" My approach to practice question #7.2 """


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_inside(self, x, y):
        return (self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2)

    def disp(self):
        print(f'x1: {self.x1}, y1: {self.y1}, x2: {self.x2}, y2: {self.y2}')

    def intersect(self, rect):
        intersect_left = self.x1 if self.x1 > rect.x1 else rect.x1
        intersect_right = self.x2 if self.x2 < rect.x2 else rect.x2
        intersect_top = self.y1 if self.y1 < rect.y1 else rect.y1
        intersect_bottom = self.y2 if self.y2 > rect.y2 else rect.y2

        if (intersect_left <= intersect_right) and (intersect_top <= intersect_bottom):
            self.x1 = intersect_left
            self.y1 = intersect_top
            self.x2 = intersect_right
            self.y2 = intersect_bottom
            return self
        else:
            return None


r1 = Rectangle(10, 10, 20, 20)
r1.disp()

print('Inside' if r1.is_inside(12, 14) else 'Not Inside')

r2 = Rectangle(15, 15, 30, 30)
r3 = r1.intersect(r2)
r3.disp()
