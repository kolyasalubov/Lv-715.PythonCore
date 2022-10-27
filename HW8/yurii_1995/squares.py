# home work 8, task 1

from math import pi, pow

def calculate_rectangle_area(width: int, length: int) -> int:
    """This function calculates an area of the rectangle
    The formula is S = width * length
    """

    rec_area = width * length

    return rec_area

def calculate_triangle_area(side: int, height: int) -> int:
    """This function calculates an area of the simple triangle.
    The formula is S = 0.5 * side * height
    """

    triangle_area = 0.5 * side * height

    return triangle_area

def calculate_circle_area(r: int) -> int:
    """This function calculates an area of the circle
    The formula is S = pi * r**2
    """

    circle_area = round(pi * pow(r, 2))

    return circle_area

