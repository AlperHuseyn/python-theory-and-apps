""" My approach to practice question #8.1, Array class """


class Array(object):
    def __init__(self, *args):
        self.array = []
        for arg in args:
            self.array.extend(arg) if isinstance(arg, (list, tuple)) else self.array.append(arg)

    def add(self, val):
        if isinstance(val, (list, tuple)):
            for elem in val:
                self.array.append(elem)
        else:
            self.array.append(val)

    def __repr__(self):
        s = ''
        for idx, elem in enumerate(self.array):
            if idx:
                s += ', '
            s += str(elem)
        print(s)


a = Array(1, 2, [3, 4, 5], 6, [7, 8])

a.__repr__()
a.add('ali')
a.__repr__()
a.add((1, ))
a.__repr__()
