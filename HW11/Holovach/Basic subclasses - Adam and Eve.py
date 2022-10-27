def God():

    def __init__(self):
        self.adam = Man()
        self.eva = Woman()
        
    def creation(self):
        return self.adam, self.eva

 


def Human():
    pass


def Man(Human):
    pass


def Woman(Human):
    pass

print(God().creation())