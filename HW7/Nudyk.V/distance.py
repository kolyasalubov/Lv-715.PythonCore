# Given two ordered pairs calculate the distance between them. 
# Round to two decimal places. This should be easy to do in 0(1) timing.

# Defined a function
def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2+(y2-y1)**2)**0.5   # formula for the dist between points
    return round(d, 2)                 # return the rounded val by 2

# Print the result
print(distance(1, 1, 0, 0))

