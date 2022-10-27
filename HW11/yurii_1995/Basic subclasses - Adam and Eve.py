# Basic subclasses - Adam and Eve

class Human:
    def __init__(self, type = "human"):
        self.type = "human"
        

class Man(Human):
    def __init__(self, name, sex = "male"):
        super().__init__()
        self.name = name
        self.sex = sex
        
        
class Woman(Human):
    def __init__(self, name, sex = "female"):
        super().__init__()
        self.name = name
        self.sex = sex
        
def God():
    man = Man("Adam")
    woman = Woman("Eve")
    human = list()
    human.append(man)
    human.append(woman)
    return human
    