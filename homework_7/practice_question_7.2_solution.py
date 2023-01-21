""" Instructor solution to practice question #7.2 """


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
        left = max(self.x1, rect.x1)
        right = min(self.x2, rect.x2)
        top =  min(self.y1, rect.y1)
        bottom = max(self.y2, rect.y2)

        return Rectangle(left, top, right, bottom) if (left <= right) and (top <= bottom) else None

r1 = Rectangle(10, 10, 20, 20)
r1.disp()

print('Inside' if r1.is_inside(12, 14) else 'Not Inside')

r2 = Rectangle(15, 15, 30, 30)
r3 = r1.intersect(r2)
if r3:
    r3.disp()
else:
    print('No intersection.')
