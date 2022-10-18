# Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as 
# string and an age as number, complete the get 
# Info property and getInfo method/Info getter which should return 
# johns age is 34



class Person():
    def __init__(self, name, age):
        self.info = f'{name}s age is {age}'


class Person_2():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return (f'{self.name}s age is {self.age}')


name = Person("matt", 25)
name_2 = Person_2("matt", 25)

print(name.info)
print(name_2.info())