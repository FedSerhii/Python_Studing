class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def drive(self, mile):
        if self.mileage + mile <= 300000:
            self.mileage += mile
        else:
            print('You can not drive more')


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car.get_mileage())

car.drive(100)
print(car.get_mileage())

car.drive(300000)
