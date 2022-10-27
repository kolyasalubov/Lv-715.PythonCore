import math


def rectangle_area():
    length = int(input("Enter rectangle's length:"))
    width = int(input("Enter rectangle's width:"))
    return length*width

def triangle_area():
    base = int(input("Enter triangle's base:"))
    hight = int(input("Enter triangle's hight:"))
    return 0.5*base*hight

def circle_area():
    radius = int(input("Enter circle's radius:"))
    return round(math.pi * math.pow(radius,2))
