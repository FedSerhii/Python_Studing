class Person:
    def __init__(self):
        self.__name = None
        self.__age = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

person = Person()

person.set_name('Serhii')
person.set_age(29)
print(person.get_name())
print(person.get_age())