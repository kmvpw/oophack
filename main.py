import random


class Thing:
    def __init__(self, name, defence_percent, attack, life):
        self.name = name
        self.defence_percent = defence_percent
        self.attack = attack
        self.life = life


class Person:
    def __init__(self, name, hp, base_attack, base_defence_percent):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defence_percent = base_defence_percent
        self.things = []

    def set_things(self, things):
        self.things = things

    def calculate_defence(self):
        '''Защита defender'''

        finalProtection = self.base_defence_percent
        for thing in self.things:
            finalProtection += thing.defence_percent
        return finalProtection

    def calculate_hp(self):
        hp = self.hp
        for thing in self.things:
            hp += thing.life
        return hp

    def calculate_attack(self):
        '''Атака attacker'''

        attack_damage = self.base_attack
        for thing in self.things:
            attack_damage += thing.attack
        return attack_damage

    def take_damage(self, damage):
        defence_percent = self.calculate_defence()
        attack_damage = damage - damage * defence_percent
        self.hp -= attack_damage
        if self.hp < 0:
            self.hp = 0


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_defence_percent):
        super().__init__(name, hp, base_attack, base_defence_percent)
        self.hp *= 2
        self.base_defence_percent *= 2


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_defence_percent):
        super().__init__(name, hp, base_attack, base_defence_percent)
        self.base_attack *= 2


things = []

for i in range(random.randint(4, 10)):
    name = f'Вещь {i}'
    life = random.randint(1, 50)
    attack = random.randint(1, 15)
    defence_percent = random.uniform(0, 0.1)
    things.append(Thing(name, defence_percent, attack, life))

names = ['Alice', 'Bob', 'Charlie', 'David', 'Ella', 'Frank', 'Grace', 'Henry', 'Isabel', 'Jack', 'Kate', 'Liam', 'Mia', 'Noah', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Sam', 'Tom']
choice_character = [Paladin, Warrior]
characters = []

for i in range(10):
    name = random.choice(names)
    hp = random.randint(50, 100)
    base_attack = random.randint(5, 20)
    base_defence_percent = random.uniform(0, 0.2)
    character = random.choice(choice_character)
    characters.append(character(name, hp, base_attack, base_defence_percent))


for character in characters:
    number_of_things = random.randint(1, 4)
    character.set_things(random.sample(things, number_of_things))

while len(characters) > 1:
    attacker = random.choice(characters)
    defenders = [character for character in characters
                 if character != attacker]
    defender = random.choice(defenders)

    attack_damage = attacker.calculate_attack()
    finalProtection = defender.calculate_defence()
    damage = attack_damage - (attack_damage * finalProtection)

    print(f'{attacker.name} наносит удар по {defender.name} на {damage} урона')

    if defender.hp == 0:
        print(f'Герой {defender.name} выбывает из поебинка!')
        characters.remove(defender)
    else:
        defender.take_damage(damage)

print(f'Победитель {characters[0].name}')
