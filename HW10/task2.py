class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello, {self.name}"

    def get_info(self):
        return "It's Homosapiens"

    @staticmethod
    def message():
        print("information")


h1 = Human("Michael")
h2 = Human("Vince")
print(h1.hello())
print(h2.hello())
print(h1.get_info())
print(h2.get_info())
h1.message()
h2.message()
Human.message()
