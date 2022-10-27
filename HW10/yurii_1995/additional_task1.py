# class work 10, task 1

class Car:
    """This class is for car object creation"""

    def __init__(self, name, kind, model, engine = "off") -> None:
        self.name = name
        self.kind = kind
        self.model = model
        self.engine = engine

    def start_car(self):
        """The method returns info when car starting"""
        if self.engine == "on":
            print(f"The car {self.name} is starting now.")

    def stop_car(self):
        """The method returns info when car stopped"""
        if self.engine == "off":
            print(f"The car {self.name} is stopped.")

car = Car("My car", "sedan", "Audi")
car_2 = Car("My second car", "sedan", "Citroen", "on")
car.start_car()
car_2.start_car()
car.stop_car()
car_2.stop_car()
