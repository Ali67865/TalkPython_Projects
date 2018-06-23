import random


class Wizard:
    def __init__(self, the_name, the_level):
        self.name = the_name
        self.level = the_level

    def attack(self, creature):
        print('{} is attacking {}'.format(self.name, creature.name))
        my_roll = random.randint(1,12) * self.level
        creature_roll = random.randint(1,12) * creature.level

        print('You roll {}; {} rolled {}...'.format(my_roll, creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('{} has defeated {}'.format(self.name, creature.name))
            return True
        else:
            print('{} has been defeated'.format(self.name))
            return False

class Creature:
    # level
    # name
    def __init__(self, the_name, the_level=10):
        self.name = the_name
        self.level = the_level

    def __repr__(self):
        return "Creature {}, level {}".format(self.name, self.level)


