# Write a program that calculates the area of ​a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).


def rectangle_area():
    ''' 
        Function to calculate the area of a rectangle.
        Does not check if the figure is a square, trapeze or diamond.
        To run the program just enter the sides of the rectangle.
    '''

    A = int(input('Enter the first side: '))
    B = int(input('Enter the second side: '))
    return print('Rectangle area = ', A * B)

def triangle_area():
    ''' 
        Function to calculate the area of certain type of triangle:
        Equilateral, Isoceles, Scalene.
        The function does not depend on the angle's inside.
        To use you need to enter the sides of the triangle.
    '''

    side_A = int(input('Enter the first side: '))
    side_B = int(input('Enter the second side: '))
    side_C = int(input('Enter the third side: '))

    if side_A == side_B == side_C:
        return print('Triangle area = ', round(side_A**2 * 3**0.5) / 4)
    elif side_A == side_B and side_A != side_C:
        Height = (side_A**2 - (side_C/2)**2)**0.5
        return print('This is a Isoceles triangle with area = ', round(((side_C*Height) / 2), 2))
    else:
        half_P = (side_A + side_B + side_C) / 2
        S_area = (half_P*(half_P - side_A)*(half_P - side_B)*(half_P - side_C))**0.5
        return print('The Scalene triangle\'s area is: ', round(S_area, 2))

def circle_area():
    ''' 
        Function to calculate the area of a circle.
        Uses only the radius of the circle.
        To run the program just enter the radius of the given circle.
    '''

    Pi = 3.14159
    radius = int(input('Please enter the radius of the circle: '))
    return print('The circle\'s area is: ', round((Pi*radius**2), 2))

def main():
    ''' 
        Fucnction to run the program
    '''

    user_choice = input("Area of what figure do you want to calculate? ")
    user_choice.lower()
    if user_choice == 'rectangle':
        return rectangle_area()
    elif user_choice == 'circle':
        return circle_area()
    elif user_choice == 'triangle':
        return triangle_area() 
    else:
        print('You entered something out of this world !!!')
        
          
main()




# First version of the triangle_area
    # triangle_type = input('What is the type of your triangle? (one word or first letter): ')
    # user_input = triangle_type.lower()

    # if user_input == 'equilateral' or user_input == 'e':
    #     return print('Triangle area = ', round(side_A**2 * 3**0.5) / 4)
    # elif user_input == 'isoceles' or user_input == 'i':
    #     if side_A == side_B:
    #         Height = (side_A**2 - (side_C/2)**2)**0.5
    #         return print('Triangle area = ', round(((side_C*Height) / 2), 2))
    #     elif side_A == side_C:
    #         Height = (side_A**2 - (side_B/2)**2)**0.5
    #         return print('Triangle area = ', round(((side_B*Height) / 2), 2))
    #     else:
    #         Height = (side_B**2 - (side_A/2)**2)**0.5
    #         return print('Triangle area = ', round(((side_A*Height) / 2), 2))
    # else:
    #     half_P = (side_A + side_B + side_C) / 2
    #     S_area = (half_P*(half_P - side_A)*(half_P - side_B)*(half_P - side_C))**0.5
    #     return print('The Scalene triangle\'s area is: ', round(S_area, 2))
