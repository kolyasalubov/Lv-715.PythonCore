# home work 10, task 1

class Polygon:
    """This class is for polygons creation"""

    def __init__(self, num_sides: list) -> None:
        self.num_sides = [input("Enter the side: ") for side in range(num_sides)]


class Rectangle(Polygon):
    """This class is for rectangles creation"""

    def __init__(self, num_sides: list) -> None:
        super().__init__(num_sides)
        self.a = int(self.num_sides[0])
        self.b = int(self.num_sides[-1])

    def get_square(self) -> int:
        """This method calculates the rectangle object square and returns it"""
        square = self.a * self.b
        return square

try:
    rectangle = Rectangle(int(input("Please type a number of sides your polygon consists of: ")))
    print(f"The square of gotting rectangle is: {rectangle.get_square()}")
except ValueError:
    print("You have typed not integer! ")
