import random


class Dice:  # simulates a player's randomization tool to accumulate random values during the game.
    def __init__(self, sides):
        self.sides = sides
        self.value = 0

    def roll(self):
        self.value = random.randint(1, self.sides+1)

    def get_value(self):
        return self.value
