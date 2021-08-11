"""
This program simulates a dice rolling game
with user-defined number of players and their names.
Once a user provides the pre-requested details,
the program will simulate the game automatically
and will output the name of player with highest accumulated
score.
"""
from Game import Game
import datetime


def main():

    begin_time = datetime.datetime.now()  # to keep track of total program duration.

    dice_game = Game()
    dice_game.data()
    dice_game.game_on()

    print("Total program runtime: {}".format(datetime.datetime.now() - begin_time))


if __name__ == '__main__':
    main()
