import random

HIT_POINTS = 100
ATTACK_DAMAGE = 10
NAMES = [
    'Alexander', 'Isabella', 'Liam', 'Olivia', 'Ethan', 'Sophia', 'Mason',
    'Ava', 'Logan', 'Mia', 'Lucas', 'Amelia', 'Jackson', 'Harper', 'Aiden',
    'Evelyn', 'Noah', 'Abigail', 'James', 'Emily'
]
NUM_CHARACTER = 10
NUM_THING = 40
THINGS_CONSTRAINTS = 4
THINGS = [
    'sword', 'shield', 'armor', 'helmet', 'ring', 'rod', 'scroll', 'staff',
    'wand'
]
NUMBER_OF_FIGHTERS = 2


class Thing:

    def __init__(self, name, defence, hit_points, attack_damage) -> None:
        self.name = name
        self.defence = defence
        self.hit_points = hit_points
        self.attack_damage = attack_damage

    def __str__(self):
        return f'{self.name}'


class Person:

    def __init__(self, name, hit_points, attack_damage, defence) -> None:
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.defence = defence
        self.things = []

    def set_things(self, things):
        for thing in things:
            self.things.append(thing)
            self.hit_points = round(self.hit_points + thing.hit_points, 2)
            self.attack_damage += thing.attack_damage
            self.defence = round(self.defence + thing.defence, 2)

    def update_hit_points(self, attack_damage):
        self.hit_points = round(
            self.hit_points - attack_damage - attack_damage * self.defence, 2)


class Paladin(Person):

    def __init__(self, name, hit_points, attack_damage, defence) -> None:
        hit_points *= 2
        defence *= 2
        super().__init__(name, hit_points, attack_damage, defence)

    def __str__(self):
        return f'Паладин {self.name} [{self.hit_points}, {self.attack_damage}, {self.defence}]'
    
    def __repr__(self) -> str:
        return f'Воин {self.name}'


class Warrior(Person):

    def __init__(self, name, hit_points, attack_damage, defence) -> None:
        attack_damage *= 2
        super().__init__(name, hit_points, attack_damage, defence)

    def __str__(self):
        return f'Воин {self.name} [{self.hit_points}, {self.attack_damage}, {self.defence}]'
    
    def __repr__(self) -> str:
        return f'Воин {self.name}'


def create_things():
    things = []
    for i in range(NUM_THING):
        name = random.choice(THINGS)
        attack = random.randint(10, 100)
        health = random.randint(10, 100)
        defence = round(random.uniform(0.01, 0.10), 2)
        thing = Thing(name, defence, health, attack)
        things.append(thing)
    sorted(things, key=lambda x: x.defence)
    return things


def create_character(things):
    characters = []
    for i in range(NUM_CHARACTER):
        name = random.choice(NAMES)
        defence = round(random.uniform(0.01, 0.10), 2)
        if random.choice([True, False]):
            character = Paladin(name, HIT_POINTS, ATTACK_DAMAGE, defence)
        else:
            character = Warrior(name, HIT_POINTS, ATTACK_DAMAGE, defence)
        things = random.sample(things, 4)
        character.things.append(things)
        character.set_things(things)
        characters.append(character)
    return characters


def main():
    print('Добро пожаловать на Арену!')
    things = create_things()
    characters = create_character(things)
    while True:
        if len(characters) == 1:
            break
        print('..........Список участников.............')
        for character in characters:
            print(character)
        print('........................................')
        attacker = characters.pop(random.randint(0, len(characters) - 1))
        print(characters)
        defender = characters.pop(random.randint(0, len(characters) - 1))
        print(f'....Сражение {attacker.name} с {defender.name}....')

        while defender.hit_points > 0:
            defender.update_hit_points(attacker.attack_damage)
            print(
                f'{attacker.name}, нанёс урон {defender.name}: {attacker.attack_damage}'
            )
            if defender.hit_points <= 0:
                characters.append(attacker)
                print(f'Победитель {attacker}')
                break
            attacker, defender = defender, attacker
            if len(characters) == 1:
                break
    winner = characters[0]
    print(f'...........{winner} победитель арены...............')


if __name__ == '__main__':
    main()
