# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square of rectangle.

class Polygon:

    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def inputSides(self):
        self.sides = [
            float(input(f'Enter side{str(i+1)}: ')) for i in range(self.n)]


class Rectangle(Polygon):

    def __init__(self):
        super().__init__(2)

    def findAreaRectangle(self):
        a, b = self.sides
        area = a * b
        print(f'Area of the rectangle is {area}')


r = Rectangle()
r.inputSides()
r.findAreaRectangle()
