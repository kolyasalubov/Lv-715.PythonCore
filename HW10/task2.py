class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Привіт, {self.name}"

    def get(self):
        return "Це Homosapiens"

    @staticmethod
    def information():
        print("Інформація")


t1 = Human("Ostap")
print(t1.hello())
print(t1.get())
t1.information()
Human.information()