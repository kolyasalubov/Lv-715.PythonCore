import areas_functions as af

def areas_calculation():

    while 1:

        figure = input("Choose the figure (1 - rectangle, 2 - triangle, 3 - circle):")

        if figure in ('1','2','3'):
            break
        print("Chose appropriate figure")
    
    match figure:
        case '1':
            return f"Rectangle's area is - {af.rectangle_area()}"
        case '2':
            return f"Triangle's area is - {af.triangle_area()}"
        case '3':
            return f"Circle's area is - {af.circle_area()}"
        case _:
            return "Error"

print(areas_calculation())