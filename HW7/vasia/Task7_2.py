import math

def rectangle():
    '''This function calculates the area of a rectangle'''
    length= float(input("Enter the length of the rectangle:"))
    width= float(input("Enter the width of the rectangle:"))
    return length*width
def triangle():
    '''This function calculates the area of a triangle'''
    a= float(input("Enter first side:"))
    b= float(input("Enter second side:"))
    c= float(input("Enter third side:"))
    #Calculation of the semi-perimeter(Обрахунок півпериметру)
    p= (a+b+c)/2
    s= math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
def circle():
    '''This function calculates the area of a circle'''
    r=float(input("Enter the radius of the circle:"))
    return math.pi*(r**2)


choice = input("Enter geometric figure (rectangle, triangle or circle):")
if choice=='rectangle':
    print(f"Rectangle area ={rectangle()}")
elif choice=='triangle':
    print(f"Triangle area ={triangle()}")
elif choice=='circle':
    print(f"Circle area ={circle()}")
