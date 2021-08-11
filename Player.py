from Dice import Dice


class Player:  # simulates a game contestant.
    def __init__(self, _name):
        self.name = _name
        self.score = 0
        self.dice = Dice(6)

    def play(self):  # accumulating the value of another dice roll result
        self.dice.roll()
        self.score += self.dice.get_value()

    def get_score(self):  # returning current score of a player.
        return self.score

    def get_name(self):
        return self.name
