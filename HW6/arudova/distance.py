'''Given two ordered pairs calculate the distance between them. 
Round to two decimal places. This should be easy to do in 0(1) timing.'''
def distance(x1, y1, x2, y2):
    a = float(((x2-x1)**2 + (y2-y1)**2) ** 0.5)
    return round(a,2)
print(distance(5, 1, 5, 0))