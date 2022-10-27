class Poligon():
    pass

class Rectangle(Poligon):

    # def __init__(self, width, length):
    #     self.square = width*length
    #     print(self.square)

    def square_count(self, width, length):
        return width*length


# Rectangle(5,5)        #25
# rec = Rectangle(4,4)  #16
# print(rec.square)     #16

rec = Rectangle()
print(rec.square_count(6,6))
