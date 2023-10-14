from dataclasses import dataclass
import random

from colorama import init, Fore, Style


CHARACTER_PULL = [
    'James',
    'Donatello',
    'Michelangelo',
    'Leondardo',
    'Rafael',
    'Shredder',
    'Kitana',
    'Ray Liotta',
    'John Travolta',
    'Michael Kane',
    'Kano',
    'Joker',
    'Cratos',
    'Antonio Banderas',
    'Britney Spears',
    'John Lennon',
    'Paul McCartney',
    'Ringo Starr',
    'George Harrison',
    'David Bowie'
]

WEAPONS_PULL = [
    'Sting',
    'Decapitator',
    'Freezer',
    'Ice Cream',
    'Spoon',
    'Flower',
    'Killersmile',
    'Rocketlauncher'
]

@dataclass
class Thing:
    '''Класс предмета'''
    name: str
    defence_bonus: float
    attack_bonus: int
    hp_bonus: int


@dataclass
class Person:
    '''Класс персонажа'''
    name: str
    defence: float
    attack: int
    hp: int

    def set_things(self, things):
        self.defence += things.defence_bonus
        self.attack += things.attack_bonus
        self.hp += things.hp_bonus

    def take_attack(self, attack):
        self.hp = self.hp - (attack - attack * self.defence)


class Paladin(Person):
    '''Класс паладина'''
    def __init__(self, name, defence, attack, hp):
        super().__init__(name, defence, attack, hp)
        self.hp *= 2
        self.defence *= 2


class Warrior(Person):
    '''Класс воина'''
    def __init__(self, name, defence, attack, hp):
        super().__init__(name, defence, attack, hp)
        self.attack *= 2


class Elf(Person):
    '''Класс эльфа'''
    def take_attack(self, attack):
        '''Логика уворота от атаки'''
        if random.randint(0, 100) > 5:
            self.hp = self.hp - (attack - attack * self.defence)
        else:
            print(Fore.YELLOW + f'{self.name} увернулся. Урон не получен.')

CHAR_TYPES = (Paladin, Warrior, Elf)

def create_characters():
    chars = []
    for _ in range(10):
        defence_calc = random.randint(0, 30)/100
        attack_calc = random.randint(5, 12)
        hp_calc = random.randint(20, 40)
        name = random.choice(CHARACTER_PULL)
        chars.append(random.choice(CHAR_TYPES)(name, defence_calc,
                                               attack_calc, hp_calc))
    return chars


def create_weapons():
    weapons = []
    for i in WEAPONS_PULL:
        item_defence_calc = random.randint(0, 10)/100
        item_attack_calc = random.randint(4, 7)
        item_hp_calc = random.randint(3, 6)
        weapons.append(Thing(i, item_defence_calc,
                             item_attack_calc, item_hp_calc))
    weapons = sorted(weapons, key=lambda i: i.defence_bonus)
    return weapons


def assign_weapons(chars, weapons):
    for character in chars:
        weapons_rand_count = random.randint(1, 4)
        for _ in range(weapons_rand_count):
            weapon_chosen = random.choice(weapons)
            character.set_things(weapon_chosen)


def main():
    init()
    all_persons = create_characters()
    answer = input('Хотите создать своего персонажа (y/N): ')
    if answer == 'y':
        name = input('Введите имя: ')
        person_cls = input('Напиши название класса Paladin, Warrior, Elf: ')
        defence_calc = random.randint(0, 30)/100
        attack_calc = random.randint(5, 12)
        hp_calc = random.randint(20, 40)
        if person_cls == 'Paladin':
            char_type = Paladin
        elif person_cls == 'Warrior':
            char_type = Warrior
        else:
            char_type = Elf
        all_persons.append(char_type(name, defence_calc, attack_calc, hp_calc))        
    all_weapons = create_weapons()
    assign_weapons(all_persons, all_weapons)

    while len(all_persons) > 1:
        attacker = random.choice(all_persons)
        defender = attacker
        while attacker == defender:
            defender = random.choice(all_persons)
        print(Fore.RED + f'{attacker.name} ', end='')
        print(Fore.WHITE + 'наносит удар по ', end='')
        print(Fore.GREEN + f'{defender.name} ', end='')
        print(Fore.WHITE + f'на {attacker.attack} урона')
        defender.take_attack(attacker.attack)
        if defender.hp <= 0:
            fallen = all_persons.pop(all_persons.index(defender))
            print(Fore.MAGENTA + f'{fallen.name} повержен!')
    print(Fore.GREEN + Style.BRIGHT + f'Победитель {all_persons[0].name}!')


if __name__ == '__main__':
    main()
