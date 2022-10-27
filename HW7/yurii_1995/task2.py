# home work 7, task 2

from cmath import pi

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

    circle_area = round(pi * r**2)

    return circle_area

def choice_figure(area_to_calculate: str) -> int:
    """This function returns an area of the user's figure"""

    if area_to_calculate == "rectangle":
        width = int(input("Please type a width of a rectange - "))
        length = int(input("Please type a length of a rectange - "))
        return calculate_rectangle_area(width, length)
    elif area_to_calculate == "triangle":
        side = int(input("Please type a side of a triangle - "))
        height = int(input("Please type a height of a triangle - "))
        return calculate_triangle_area(side, height)
    elif area_to_calculate == "circle":
        r = int(input("Please type a radious of a circle - "))
        return calculate_circle_area(r)
    else:
        return "You have typed a title of a figure not correct. Please type again later"
        

area_to_calculate = input("What area would you like to calculate? (rectangle, triangle or circle) - ")
print(choice_figure(area_to_calculate))