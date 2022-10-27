class Ball:
    def __init__(self, ball_type=None):
        self.__ball_type = ball_type

    def ball_type(self):
        if not self.__ball_type:
            print("regular")
        else:
            print(self.__ball_type)


ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type()  # => "regular"
ball2.ball_type()  # => "super"
