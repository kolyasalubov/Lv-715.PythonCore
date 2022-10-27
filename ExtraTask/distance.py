import math


def search_dist(XA, YA, XB, YB):
    return math.sqrt((XB - XA) ** 2 + (YB - YA) ** 2)


A = input('Enter coordinates of the first point with space ')
B = input('Enter coordinates of the first point with space ')

XA, YA = A.split()
XB, YB = B.split()
XA, YA = int(XA), int(YA)
XB, YB = int(XB), int(YB)

dist = search_dist(XA, YA, XB, YB)
print(f"distance between A and B = {dist}")
