class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Rectangle(Polygon):
    def square(self):
        return self.a * self.b


r1 = Rectangle(4, 5)
print(r1.square())
