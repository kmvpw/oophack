from random import randint


class Thing():
    def __init__(self, name, defense=0, attack=0, hp=0) -> None:
        self.name = name
        self.defense = defense
        self.attack = attack
        self.hp = hp

    def create_things():
        armor_defenses = []
        armor_hps = []
        weapon_attack = []
        ring_hps = []
        n = 10
        for i in range(n):
            armor_defenses.append(randint(0, 10))
            armor_hps.append(randint(10, 30))
            weapon_attack.append(randint(5, 15))
            ring_hps.append(randint(15, 50))
        armor_defenses = sorted(armor_defenses)
        armor_names = [f'armor{index}' for index in range(1, 11)]
        weapon_names = [f'weapon{index}' for index in range(1, 11)]
        ring_names = [f'ring{index}' for index in range(1, 11)]
        random = randint(10, 20)
        armors_amount = (random // 3) + (random % 3)
        weapons_amount = random // 3
        rings_amount = random // 3
        things = []

        for index in range(weapons_amount):
            things.append(Thing(name=weapon_names[index],
                          attack=weapon_attack[index]))
        for index in range(ring_names):
            things.append(Thing(name=ring_names[index], hp=rings_amount[index]))
        for index in range(armors_amount):
            things.append(Thing(name=armor_names[index],
                          defense=armor_defenses[index],
                          hp=armor_hps[index]))
        things.shuffle()
