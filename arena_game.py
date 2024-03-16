from random import choice, randint, uniform, sample

NAMES = [
    "Azura", "Caspian", "Elysia", "Finnian", "Isolde", "Lysander",
    "Maeve", "Orion", "Persephone", "Soren", "Thalia", "Vesper",
    "Xanthe", "Zephyr", "Aurelia", "Cyrus", "Dahlia", "Ezra",
    "Nova", "Ragnar"
]


class Thing:
    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp


all_things = [
    Thing("Armor", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Chain mail", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Sword", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Helmet", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Boots", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Belt", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Ring", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Staff", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Amulet", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
]


class Person:
    def __init__(self):
        self.chr_name = NAMES.pop()
        self.chr_hp = 100
        self.chr_armor = 0.1
        self.chr_attack = 10
        self.equipped_things = []

    def set_things(self, things):
        for thing in things:
            self.equipped_things.append(thing)
            self.chr_armor += thing.protection
            self.chr_attack += thing.attack
            self.chr_hp += thing.hp

    def subtract_hp(self, attack):
        self.damage_taken = round(attack - attack*self.chr_armor, 2)
        self.chr_hp -= self.damage_taken


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.chr_hp *= 2
        self.chr_armor *= 2


class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.chr_attack *= 2


def main():
    # Логика игры
    # Создаем 10 персонажей
    players = []
    i = 0
    while i < 10:
        players.append(choice((Paladin(), Warrior())))
        i += 1

    for player in players:
        player.set_things(sample(all_things, randint(1, 4)))

    running = True

    while running:
        fighters = sample(players, k=2)
        attacking, defending = fighters
        while attacking.chr_hp > 0 and defending.chr_hp > 0:
            defending.subtract_hp(attacking.chr_attack)
            print(
                f'{attacking.chr_name} наносит удар по {defending.chr_name}'
                f' на {defending.damage_taken} урона')

            # Удаляем проигравшего
            if defending.chr_hp <= 0:
                players.remove(defending)
                break

            attacking, defending = defending, attacking

        # Проверяем, остался ли 1 игрок и завершаем игру
        if len(players) == 1:
            running = False
            print(f'Игра окончена, победил игрок {players[0].chr_name}')


if __name__ == '__main__':
    main()
