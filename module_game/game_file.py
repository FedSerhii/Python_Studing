from enum import Enum
from random import randint
import time
import sys


class SelectionType(Enum):
    WARRIOR = 1
    ARCHER = 2
    WIZARD = 3
    RIDER = 4


class Character:
    def __init__(self, name, health_point, damage, crit, luck, faction, level=1):
        self.name = name
        self.current_health = health_point
        self.health_point = health_point
        self.damage = damage
        self.crit = crit
        self.luck = luck
        self.faction = faction
        self.level = level



    def __str__(self):
        return (f'\n'
                f'{self.name}\n'
                f'Health Point: {self.health_point}\n'
                f'Damage: {self.damage}\n'
                f'Critical Damage: {self.crit}\n'
                f'Luck: {self.luck}\n'
                f'Level: {self.level}\n'
                f'Faction: {self.faction}')

    def real_damage(self):
        luck = randint(1, 100)
        if luck <= self.luck:
            crit_damage = self.damage + self.damage * self.crit
            return crit_damage
        else:
            return self.damage

    def level_up(self):
        self.health_point = round(self.health_point * 1.15)
        self.damage = round(self.damage * 1.1)
        self.luck -= 5
        self.level += 1

    def level_down(self):
        if self.level > 1:
            self.health_point = round(self.health_point / 1.15)
            self.damage = round(self.damage / 1.1)
            self.luck += 5
            self.level -= 1

    def restore_health(self):
        self.current_health = self.health_point


class Warrior(Character):
    def __init__(self):
        super().__init__('Warrior', 4500, 200, 0.35, 55, 'Red')

    def punch(self, enemy):
        if isinstance(enemy, Wizard):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


class Archer(Character):
    def __init__(self):
        super().__init__('Archer', 3000, 285, 0.45, 40, 'White')

    def punch(self, enemy):
        if isinstance(enemy, Rider):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


class Rider(Character):
    def __init__(self):
        super().__init__('Rider', 4000, 220, 0.25, 68, 'Blue')

    def punch(self, enemy):
        if isinstance(enemy, Warrior):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


class Wizard(Character):
    def __init__(self):
        super().__init__('Wizard', 2600, 370, 0.5, 30, 'Red')

    def punch(self, enemy):
        if isinstance(enemy, Archer):
            return self.real_damage() + (self.damage * 0.15)
        else:
            return self.real_damage()


def char(char_type: SelectionType):
    char_dict = {
        SelectionType.WARRIOR: Warrior,
        SelectionType.ARCHER: Archer,
        SelectionType.WIZARD: Wizard,
        SelectionType.RIDER: Rider
    }
    return char_dict[char_type]()


characters = [char(SelectionType.WARRIOR),
              char(SelectionType.ARCHER),
              char(SelectionType.WIZARD),
              char(SelectionType.RIDER)]


class Game:
    def menu(self):
        while True:
            print('Press 1 to fight one on one\n'
                  'Press 2 to fight Army on Army\n'
                  'Press 3 to view attributes\n'
                  'Press 0 to exit')

            button = int(input('What will we do next: '))
            match button:
                case 1:
                    self.chose_char()
                case 2:
                    self.battle_army()
                case 3:
                    print('View attributes:\n')
                    for character_type in SelectionType:
                        pers1 = char(character_type)
                        time.sleep(1)
                        print(f'Pers type: {pers1.name}')
                        print(pers1)
                        print('-----------------------')
                case 4:
                    print('Thank you. Bye:)')
                    sys.exit()
                case _:
                    print('Incorrect input, please try again')
                    self.menu()

    @staticmethod
    def select_character():
        print('Please, choose your character:\n'
              'Warrior-------->Press 1\n'
              'Archer--------->Press 2\n'
              'Rider---------->Press 3\n'
              'Wizard--------->Press 4')

        choose = int(input('Please, make your choice: '))
        match choose:
            case 1:
                choose = characters[0]
            case 2:
                choose = characters[1]
            case 3:
                choose = characters[2]
            case 4:
                choose = characters[3]
            case _:
                print('Invalid input')
        return choose

    @staticmethod
    def enemy_pers():
        choice = randint(1, 4)
        return characters[choice - 1]

    @staticmethod
    def sort_characters_by_health_and_damage():
        sorted_characters = sorted(characters, key=lambda x: (x.health_point, x.damage), reverse=True)
        return sorted_characters

    def chose_char(self):
        my_pers = self.select_character()
        enemy = self.enemy_pers()
        print(f'{my_pers.name} and {enemy.name} will fight!')
        print('Press 1 to fight\n'
              'Press 2 to view attributes\n'
              'Press 3 to sort characters by Health and Damage\n'
              'Press 0 to exit')
        button = int(input('What will we do next: '))
        match button:
            case 1:
                self.fight(my_pers, enemy)
            case 2:
                print(my_pers)
                print('\nYour opponent:')
                print(enemy)
                print('-------------------')
                next_action = int(input('Press 6 to return to the menu: '))
                if next_action == 6:
                    self.further_action(my_pers, enemy)
                else:
                    print('Invalid input!')
                    sys.exit()
            case 3:
                sorted_characters = self.sort_characters_by_health_and_damage()
                print('\nSorted by Health and Damage:')
                for char in sorted_characters:
                    print(f"{char.name} - Health: {char.health_point}, Damage: {char.damage}")
                self.further_action(my_pers, enemy)
            case 0:
                print('See you next time. Bye:)')
                sys.exit()
            case _:
                print('Incorrect input! Bye:)')
                sys.exit()

    def further_action(self, my_pers, enemy):
        print('What are you want next?\n'
              'Press 1 to fight\n'
              'Press 2 to view all attributes\n'
              'Press 3 to sorted by Health and Damage\n'
              'Press 5 to return to the menu\n'
              'Press 0 to exit')
        press = int(input('What is your choice: '))
        if press == 1:
            self.fight(my_pers, enemy)
        elif press == 2:
            print(my_pers)
            print('\nYour opponent:')
            print(enemy)
            print('-------------------')
            next_action = int(input('Press 6 to return to the menu: '))
            if next_action == 6:
                self.further_action(my_pers, enemy)
            else:
                print('Invalid input!')
                sys.exit()
        elif press == 3:
            sorted_characters = self.sort_characters_by_health_and_damage()
            print('\nSorted by Health and Damage:')
            for char in sorted_characters:
                print(f"{char.name} - Health: {char.health_point}, Damage: {char.damage}")
            self.further_action(my_pers, enemy)
        elif press == 5:
            self.menu()
        elif press == 0:
            print('Thank you. Bye:)')
            sys.exit()
        else:
            print('Invalid input!')
            sys.exit()



    @staticmethod
    def fight(pers1, pers2):
        print(f'{pers1.name} will fight with {pers2.name}')
        while pers1.current_health > 0 and pers2.current_health > 0:
            pers2.current_health -= pers1.punch(pers2)
            print(f'{pers1.name} deals {pers1.punch(pers2)}\n'
                  f'{pers2.name} has {pers2.current_health} health points\n'
                  f'-------------------------------------')
            game.verification(pers1, pers2)
            time.sleep(1)

            pers1.current_health -= pers2.punch(pers1)
            print(f'{pers2.name} deals {pers2.punch(pers1)}\n'
                  f'{pers1.name} has {pers1.current_health} health points\n'
                  f'-------------------------------------')
            game.verification(pers1, pers2)
            time.sleep(1)
    @staticmethod
    def verification(my_pers, enemy):
        if my_pers.current_health <= 0:
            print('You lost! Better luck next time!')
            my_pers.level_down()
            enemy.level_up()
            my_pers.restore_health()
            enemy.restore_health()
            game.menu()
        elif enemy.current_health <= 0:
            print(f'{my_pers.name} is the winner! Congratulations!')
            my_pers.level_up()
            enemy.level_down()
            my_pers.restore_health()
            enemy.restore_health()
            game.menu()
        elif my_pers.current_health <= 0 and enemy.current_health <= 0:
            print('Well, this time it is a draw!')
            my_pers.restore_health()
            enemy.restore_health()
            game.menu()

    @staticmethod
    def army_stats(army):
        total_health = sum(pers.current_health for pers in army)
        total_damage = sum(pers.damage for pers in army)
        return total_health, total_damage

    def create_army(self, army_size):
        army = []
        print('Chose your character: ')
        for i in range(army_size):
            pers = self.select_character()
            army.append(pers)
            print(f'{pers.name} was add to the army')
        return army

    @staticmethod
    def battle_army():
        print('Create first Army:')
        army_1_size = int(input('Please enter the size of the army: '))
        first_army = game.create_army(army_1_size)

        print('\nCreate second Army:')
        army_2_size = int(input('Please enter the size of the army: '))
        second_army = game.create_army(army_2_size)

        print("Let's start our battle!\n")
        time.sleep(2)

        army1_health, army1_damage = game.army_stats(first_army)
        army2_health, army2_damage = game.army_stats(second_army)

        print(f'Total Health Point of first Army: {army1_health}, Total Damage: {army1_damage}\n'
              f'Total Health Point of second Army: {army2_health}, Total Damage: {army2_damage}\n'
              f'------------------------------------------------------------------------------')

        while army1_health > 0 and army2_health > 0:
            army2_health -= army1_damage
            print(f'The First Army dealt {army1_damage} hit points\n'
                  f'The Second Army have {army2_health} hit points\n'
                  f'----------------------------------------------')
            time.sleep(1)

            army1_health -= army2_damage
            print(f'The Second Army dealt {army2_damage} hit points\n'
                  f'The First Army have {army1_health} hit points\n'
                  f'----------------------------------------------')
            time.sleep(1)

        if army1_health <= 0:
            print('Second Army is WINNER. Congratulation!!!')
        else:
            print('First Army is WINNER. Congratulation!!!')


if __name__ == '__main__':
    game = Game()
    player = game.menu()