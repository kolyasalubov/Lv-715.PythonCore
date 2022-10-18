# Create a class Ball. 
# Ball objects should accept one argument for "ball type" when instantiated.

# If no arguments are given, ball objects should 
# instantiate with a "ball type" of "regular."


class Ball:
    '''
    This is  an instance for a Ball class
    '''
    def __init__(self, name='regular'):
        self.name = name
        print(name)

    def ball_type(self):
        print(self.name)



ball1 = Ball()
ball2 = Ball('super')

ball1.ball_type
ball2.ball_type


