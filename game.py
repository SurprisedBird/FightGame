from fight import Fight
import constants

class Game():

    fight = Fight()

    fight.print_hello(constants.warriors)
    fight.choose_warrior(constants.warriors)
    fight.choose_random_warrior(constants.warriors)
    fight.main_fight()

    win = fight.main_fight()
    if win:
        print(constants.win_message)
    else:
        print(constants.losing_message)