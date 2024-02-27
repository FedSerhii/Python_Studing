from abc import ABC

class Car(ABC):
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model


class Sedan(Car):
    def __init__(self, mark, model, count_doors):
        super().__init__(mark, model)
        self.count_doors = count_doors

    def display_info(self):
        print(f'Car: {self.mark} {self.model}\n'
              f'Doors: {self.count_doors}')


class SUV(Car):
    def __init__(self, mark, model, count_seats):
        super().__init__(mark, model)
        self.count_seats = count_seats

    def display_info(self):
        print(f'Car: {self.mark} {self.model}\n'
              f'Seats: {self.count_seats}')


class SportsCar(Car):
    def __init__(self, mark, model, max_speed):
        super().__init__(mark, model)
        self.max_speed = max_speed

    def display_info(self):
        print(f'Car: {self.mark} {self.model}\n'
              f'Max Speed: {self.max_speed} km/h')


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()