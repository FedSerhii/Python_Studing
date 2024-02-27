class Person:
    def __init__(self):
        self.__name = None
        self.__age = None

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print('Please, input your correct name')

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            print('Invalid input')

    def get_age(self):
        return self.__age

person = Person()

person.set_name('Serhii123')
person.set_age(150)
print(person.get_name())
print(person.get_age())
