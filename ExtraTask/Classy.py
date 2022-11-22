class Person:
    def __init__(self, name, age):
        self.info = f"{name}'s age is {age}"


p1 = Person("Vadym", 20)
print(p1.info)
