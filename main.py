from random import randint, uniform, choice

DEFAULT_ATTACK = 1.0
DEFAULT_DEFENCE = 0.0
DEFAULT_HEALTH = 10.0
DICT_NAME_CHARACTERS = ('Леголас', 'Арвен', 'Громовержец', 'Эльрик', 'Драконоруб', 'Шаландра', 'Скайволкер', 'Тиранда', 'Мордред', 'Архимонд')
DICT_NAME_THINGS = (
    'Меч Света','Плащ Тьмы','Свиток Великана','Шлем Героя','Посох Заклинаний','Амулет Бессмертия','Кольцо Владыки','Сапоги Путешественника','Жезл Драконов','Лук Эльфа','Доспехи Хранителя','Клинок Мстителя','Перчатки Мага','Зелье Жизни','Печать Волшебника','Руна Призыва','Дубина Титана','Скатерть Летающего Тапка','Гримуар Заклинаний','Щит Всадника','Кулон Времени','Ожерелье Защиты','Арбалет Стрелока','Амулет Оракула','Щит Героя','Меч Холодного Огня','Древо Жизни','Шлем Рыцаря','Поножи Волшебства','Клинок Искусителя','Зелье Инвизибилити','Сфера Вдохновения','Свиток Забвения','Кольцо Возрождения','Сандалии Песчаного Ветра','Оракульский Жезл','Кираса Победителя','Жезл Перемещения','Плащ Подземелий','Кулон Власти'
)
class Thing:
    
    def __init__(self, name: str, defence: float, attack:float, hp:float) -> None:
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp



class Person:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.hp = DEFAULT_HEALTH
        self.defence = DEFAULT_DEFENCE
        self.attack = DEFAULT_ATTACK


    def set_thing(self, things:list[Thing]):
        for thing in things:
            print(thing)
            self.hp += thing.hp
            self.defence += thing.defence
            self.attack += thing.attack

    def defence(self, fighter:object):
        damage = fighter.attack - fighter.attack * self.defence
        self.hp -= damage
        print(f'{fighter.name} наносит удар по {self.name} на {damage} урона')

    def __str__(self) -> str:
        return f'{self.name} - hp: {self.hp}, defence: {self.defence}, attack: {self.attack}'

class Paladin(Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.hp *= 2
        self.defence *= 2


class Warrior(Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.attack *= 2

def create_things() -> list[Thing]:
    return [(DICT_NAME_THINGS[i], uniform(0, 0.1), uniform(0, 10), uniform(0,100)) for i in range(randint(0,40))]


def create_character():
    return [choice((Paladin, Warrior))(DICT_NAME_CHARACTERS[i]) for i in range(10)]

def character_dressing(fighters:list[object], things:list[Thing])-> None:
    while things:
        choise_things = []
        character = fighters.pop(randint(0,len(fighters)-1))
        if len(things) >= 4:
            for i in range(randint(0,4)):
                choise_things.append(things.pop(randint(0, len(things) - 1)))
        else:
            for i in range(randint(0, len(things)-1)):
                choise_things.append(things.pop(randint(0, len(things) - 1)))
        character.set_thing(choise_things)


def arena_fight(warriors:list[object]):
    while len(warrroirs) > 1:
        fighter_1 = warriors.pop(randint(0,len(fighters)-1))
        fighter_2 = warriors.pop(randint(0,len(fighters)-1))
        while fighter_1.hp > 0 or fighter_2.hp > 0:
            fighter_2.defence(fighter_1)
            if fighter_2.hp > 0:
                fighter_1.defence(fighter_2)
        if fighter_1.hp > 0:
            warriors.append(fighter_1)
            continue
        warriors.append(fighter_2)


things = create_things()
characters = create_character()
print(character_dressing(characters, things))