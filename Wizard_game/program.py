import random
import time

from creatures import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------')
    print('--------WIZARD GAME--------')
    print('---------------------------')


def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from the forbidden forest...'.format(active_creature.name, active_creature.level))

        cmd = input('Do you want to [a]ttack, [l]ook around or [r]un away?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('{} has been defeated and must hide in the forest to regain his strength'.format(hero.name))
                time.sleep(5)
                print('{} has regained his strength and is ready to wander forth'.format(hero.name))
        elif cmd == 'l':
            print('{} has a look around and sees...')
            for c in creatures:
                print('     *       {} of level {}'.format(c.name, c.level))
        elif cmd == 'r':
            print('The Wizard has become unsure of his power and flees...')
        else:
            print('Exiting game, bye!')
            break


if __name__ == '__main__':
    main()
