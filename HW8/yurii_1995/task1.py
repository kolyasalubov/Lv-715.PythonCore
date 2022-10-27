# home work 8, task 1

import squares

def choice_figure(area_to_calculate: str) -> int:
    """This function returns an area of the user's figure"""

    if area_to_calculate == "rectangle":
        width = int(input("Please type a width of a rectange - "))
        length = int(input("Please type a length of a rectange - "))
        return squares.calculate_rectangle_area(width, length)
    elif area_to_calculate == "triangle":
        side = int(input("Please type a side of a triangle - "))
        height = int(input("Please type a height of a triangle - "))
        return squares.calculate_triangle_area(side, height)
    elif area_to_calculate == "circle":
        r = int(input("Please type a radious of a circle - "))
        return squares.calculate_circle_area(r)
    else:
        return "You have typed a title of a figure not correct. Please type again"
        
area_to_calculate = input("What area would you like to calculate? (rectangle, triangle or circle) - ")
print(choice_figure(area_to_calculate))