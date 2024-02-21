class Vehicle:
    def __init__(self, model, speed, coast):
        self.model = model
        self.speed = speed
        self.coast = coast

    def __gt__(self, other):
        return self.speed > other.speed

car1 = Vehicle('Toyota', 90, 12000)
car2 = Vehicle('BMW', 120, 15000)
car3 = Vehicle('Mazda', 85, 10000)
car4 = Vehicle('Audi', 115, 13500)

vehicle = [car1, car2, car3, car4]

sorted_list = sorted(vehicle, reverse=True)

for vehicle in sorted_list:
    print(f'{vehicle.model}: Speed - {vehicle.speed} km/h, Coast - {vehicle.coast}$')