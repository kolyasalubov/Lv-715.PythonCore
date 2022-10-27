class Car():

    def __init__(self, name, kind, model) -> None:
        self.name = name
        self.kind = kind
        self.model = model

    def start(self):
        print(f'Car {self.kind} - {self.name} is {self.model} started')
        
    def stop(self):
        print(f'Car {self.kind} - {self.name} is {self.model} stoped')

Car('Vasya', 'Zaporozec', 'Banderamobil').start()
Car('Vasya', 'Zaporozec', 'Banderamobil').stop()
vasya = Car('Vasya', 'Zaporozec', 'Banderamobil')
vasya.start()
vasya.stop()