class Ball():

    """
        This is balaball class)))
    """

    def __init__(self, obj = 'regular'):
        self.obj = obj

    def ball_type(self):
        return self.obj

print(Ball().ball_type())
print(Ball('super').ball_type())
print(Ball().__doc__)
#  
#     def __init__(self, type = 'regular'):
#         self.type = type


#     def ball_type(self):
#         return self.type

# print(Ball().ball_type())
# print(Ball('super').ball_type())
# # print(balaball.ball_type())
# # print(balaball.__doc__)
# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type()  #=> "regular"
# ball2.ball_type()  #=> "super"
    
    

