""" Instructor approach to practice question #8.1, Array class """


class Array(object):
    def __init__(self, *args):
        self.array = []
        for arg in args:
            if isinstance(arg, list):
                self.array.extend(arg)
            else:
                self.array.append(arg)

    def add(self, val):
        if isinstance(val, list):
            for elem in val:
                self.array.append(elem)
        else:
            self.array.append(val)

    def disp(self):
        print(*self.array, sep=', ')


a = Array(1, 2, [3, 4, 5], 6, [7, 8])

a.disp()
a.add('ali')
a.disp()
a.add([10, 20, 30, 40, 50])
a.disp()
