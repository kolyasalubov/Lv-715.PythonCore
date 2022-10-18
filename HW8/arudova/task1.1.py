import task1

k = input('figure = ')
if k == 'rectangle':
    length = int(input('length = '))
    width = int(input('width = '))
    print(task1.rectangle(length,width))
elif k == 'triangle':
    base = int(input('base = '))
    height = int(input('height = '))
    print(task1.triangle(base,height))
elif k == 'circle':
    radius = int(input('radius = '))
    print(task1.circle(radius))
else:
    print('choose rectangle,triangle or circle')