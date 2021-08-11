from Player import Player


class Game:  # main program's component. handles all players involved and their score.
    def __init__(self):
        self.rounds = 0  # holds track of a given number of rounds to be played.
        self.num_players = 0  # user-defined number of players involved
        self.players = []  # holds information of all players involved in the game.

    def data(self):  # function to get user-defined information regarding the game's behavior.

        print("Hello and welcome to the game of Dice !\n")

        self.rounds = int(input("Enter number of rounds: "))
        while self.rounds <= 0:
            self.rounds = int(input("Invalid number of rounds. Try again: "))

        self.num_players = int(input("Enter number of players: "))
        while self.num_players <= 0:
            self.num_players = int(input("Invalid number of players. Try again: "))

        for i in range(self.num_players):
            buffer = input("Enter name of player no. {}: ".format(i+1))
            while buffer == "":
                buffer = input("Invalid name given. Try again: ")
            self.players.append(Player(buffer))

    def game_on(self):  # main game's function. runs the actual game's logic.

        # main procedure. simulates dice roll rounds
        for i in range(self.rounds):
            for player in self.players:
                player.play()

        # winner finding
        max_score = 0
        winner = Player("None")

        for player in self.players:
            if player.get_score() > max_score:
                winner = player

        # outputting the game's result.
        print("Congratulations {0} ! you've won with the highest score of: {1}".format(winner.get_name(),
                                                                                       winner.get_score()))
