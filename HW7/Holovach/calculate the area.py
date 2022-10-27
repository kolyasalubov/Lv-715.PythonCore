def calculate_the_area_of_the_geometrical_figure(figure: int) -> str:

    """
    Calculate the area of rectangle, triangle and circle depending on user's choice
    """

    if figure == 1:
        return f"""The rectangle's area is - {int(input("Enter first side's length:")) * int(input("Enter second side's length:"))}"""
    elif figure == 2:
        return f"""The triangle's area is - {round((int(input("Enter button's length:")) * int(input("Enter triangle's hight:"))) / 2, 2)}"""
    elif figure == 3:
        return f"""The circle's area is - {round((int((input("Enter circle's radius:")))**2)*3.14, 2)}"""
    else:
        return "There no calculation for another figures"


print(f"""{calculate_the_area_of_the_geometrical_figure
(int(input('Chose the figure(1 - rectangle, 2 - triangle and 3 - circle:)')))}
    """)