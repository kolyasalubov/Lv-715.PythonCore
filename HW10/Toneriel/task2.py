# Create a class Human, everyone has a name, create a
# method in the class that displays a welcome message to a
# each person. Create a class method in the class that
# returns information that it is a species of "Homosapiens".
# And also in the class create a static method that returns
# an arbitrary message.

class Human:
    # Class attribute
    species = "Homosapiens"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def say(self, msg):
        return f'{self.name}: {msg}'

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def info_msg():
        return "*Static method is called without reference to a class or instance*"


man_1 = Human("Aragorn")
print(man_1.say("Hello! How are you?"))

man_2 = Human("Beren")
print(man_2.say("Hello! Where is Lúthien?"))

print(man_1.get_species())
print(man_2.get_species())


# Returns a static method
print(Human.info_msg())
