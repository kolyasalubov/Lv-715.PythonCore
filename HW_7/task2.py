

def area_rectangle(a, b):
    return a*b

def area_triangle(a, b, c):
    import math
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

def area_circle(r):
    s = 3.14 * r*r
    return s

print(area_rectangle(4, 6))
print(area_triangle(2, 4, 3))
print(area_circle(2))