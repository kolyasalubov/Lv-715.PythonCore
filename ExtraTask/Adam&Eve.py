class Human:
    @staticmethod
    def count_object():
        return [Man.COUNT_MAN, Woman.COUNT_WOMAN]


class Man(Human):
    COUNT_MAN = 0

    def __init__(self):
        self.__class__.COUNT_MAN += 1


class Woman(Human):
    COUNT_WOMAN = 0

    def __init__(self):
        self.__class__.COUNT_WOMAN += 1


w1 = Woman()
w2 = Woman()
w3 = Woman()
w4 = Woman()
print(Human.count_object())
