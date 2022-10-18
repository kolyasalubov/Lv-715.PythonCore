def rectangle(length,width):
    ''' this func returns area of rectangle'''
    return length*width

def triangle(base,height):
    ''' this func returns area of triangle '''
    return (base*height)/2

def circle(radius):
    ''' this func returns area of circle'''
    p = 3.1415
    return (p*radius)**2

k = input('figure = ')
if k == 'rectangle':
    length = int(input('length = '))
    width = int(input('width = '))
    print(rectangle(length,width))
elif k == 'triangle':
    base = int(input('base = '))
    height = int(input('height = '))
    print(triangle(base,height))
elif k == 'circle':
    radius = int(input('radius = '))
    print(circle(radius))
else:
    print('choose rectangle,triangle or circle')