# home work 10, task 2

class Human:
    """This class is for human objects creation"""

    def __init__(self, name) -> None:
        self.name = name

    def show_welcome_message(self):
        """This method displays a welcome message to an each person"""
        print(f"Welcome, {self.name}")

    @classmethod
    def show_species(cls):
        """This method returns information that it is a species of 'Homosapiens'"""
        return "Your object of this class is 'Homosapiens' species"

    @staticmethod
    def show_arbitrary_message():
        """This method returns an arbitrary message"""
        return "This message is arbitrary for class 'Human'"

person = Human("Yurii")
person.show_welcome_message()
print(person.show_species())
print(person.show_arbitrary_message())
