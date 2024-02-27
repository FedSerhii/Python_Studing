class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def display_info(self):
        return print(f'Name: {self.name}\nKind: {self.kind}')


class Mammal(Animal):
    def __init__(self, name, kind, type_of_food):
        super().__init__(name, kind)
        self.type_of_food = type_of_food

    def display_info(self):
        super().display_info()
        print(f'Type of Food: {self.type_of_food}')


class Carnivore(Mammal):
    def __init__(self, name, kind, type_of_food, teeth):
        super().__init__(name, kind, type_of_food)
        self.teeth = teeth

    def display_info(self):
        super().display_info()
        print(f'Teeth: {self.teeth}')


class Lion(Carnivore):
    def __init__(self, name, kind, type_of_food, teeth, mane):
        super().__init__(name, kind, type_of_food, teeth)
        self.mane = mane

    def display_info(self):
        super().display_info()
        print(f'Mane: {self.mane}')

lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()