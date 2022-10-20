'''Create a polygon class and a rectangle class
that inherits from the polygon class and finds the square
of rectangle'''
class Polygon:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Rectangle(Polygon):
    def square(self):
        return self.x * self.y


var = Rectangle(4, 5)
print(f'square = {var.square()}')