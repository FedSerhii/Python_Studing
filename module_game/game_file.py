from enum import Enum
from random import randint
import time


class SelectionType(Enum):
    WARRIOR = 1
    ARCHER = 2
    WIZARD = 3
    RIDER = 4


class Character:
    def __init__(self, name, health_point, damage, crit, luck):
        self.name = name
        self.health_point = health_point
        self.damage = damage
        self.crit = crit
        self.luck = luck

    def __str__(self):
        return (f'\n'
                f'{self.name}\n'
                f'Health Point: {self.health_point}\n'
                f'Damage: {self.damage}\n'
                f'Critical Damage: {self.crit}\n'
                f'Luck: {self.luck}')

    # def __gt__(self, other):
    #     return self.health_point > other.health_point

    def real_damage(self):
        luck = randint(1, 100)
        if luck <= self.luck:
            crit_damage = self.damage + self.damage * self.crit
            return crit_damage
        else:
            return self.damage


class Warrior(Character):
    def __init__(self):
        super().__init__('Warrior', 4500, 200, 0.35, 55)

    def punch(self, enemy):
        if isinstance(enemy, Wizard):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


class Archer(Character):
    def __init__(self):
        super().__init__('Archer', 3000, 285, 0.45, 40)

    def punch(self, enemy):
        if isinstance(enemy, Rider):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


class Rider(Character):
    def __init__(self):
        super().__init__('Rider', 4000, 220, 0.25, 68)

    def punch(self, enemy):
        if isinstance(enemy, Warrior):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


class Wizard(Character):
    def __init__(self):
        super().__init__('Wizard', 2600, 370, 0.5, 30)

    def punch(self, enemy):
        if isinstance(enemy, Archer):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


def create_char(selection_type: SelectionType) -> Character:
    char_dict = {
        SelectionType.WARRIOR: Warrior,
        SelectionType.ARCHER: Archer,
        SelectionType.RIDER: Rider,
        SelectionType.WIZARD: Wizard
    }
    return char_dict[selection_type]()

# def sort_by_health(characters):
#     return sorted(characters, key=lambda char: char.health_point, reverse=True)
#
# def sort_by_damage(characters):
#     return sorted(characters, key=lambda char: char.damage, reverse=True)
#
# list_of_char = [Warrior(), Archer(), Rider(), Wizard()]

def chose_character():
    print('Please, choose your character:\n'
          'Warrior-------->Press 1\n'
          'Archer--------->Press 2\n'
          'Rider---------->Press 3\n'
          'Wizard--------->Press 4')
    chose = int(input('Please, make your choice: '))
    if chose == 1:
        print('You chose a Warrior. Good luck!\n'
              '---------------------------------')
        return Warrior
    elif chose == 2:
        print('You chose an Archer. Good luck!\n'
              '---------------------------------')
        return Archer
    elif chose == 3:
        print('You chose a Rider. Good luck!\n'
              '-------------------------------')
        return Rider
    elif chose == 4:
        print('You chose a Wizard. Good luck!\n'
              '--------------------------------')
        return Wizard
    else:
        print('Invalid input')

def enemy_pers():
    chose = randint(1, 4)
    if chose == 1:
        print('Your opponent is a Warrior!\n'
              '-------------------------------')
        return Warrior
    elif chose == 2:
        print('Your opponent is an Archer!\n'
              '-------------------------------')
        return Archer
    elif chose == 3:
        print('Your opponent is a Rider!\n'
              '-------------------------------')
        return Rider
    else:
        print('Your opponent is a Wizard!\n'
              '-------------------------------')
        return Wizard


def fight(pers1, pers2):
    print(f'{pers1.name} will fight with {pers2.name}')
    while pers1.health_point > 0 and pers2.health_point >0:
        pers2.health_point -= pers1.punch(pers2)
        print(f'{pers1.name} deals {pers1.punch(pers2)}\n'
              f'{pers2.name} has {pers2.health_point} health point\n'
              f'-------------------------------------')
        time.sleep(2)
        if pers2.health_point <= 0:
            print(f'{pers1.name} is Winner! Congratulation!')
            break
        pers1.health_point -= pers2.punch(pers1)
        print(f'{pers2.name} deals {pers2.punch(pers1)}\n'
              f'{pers1.name} has {pers1.health_point} health point\n'
              f'-------------------------------------')
        time.sleep(2)
        if pers1.health_point <= 0:
            print(f'You are lose! Try next time!')
            break


first_pers = chose_character()()
second_pers = enemy_pers()()

fight(first_pers, second_pers)