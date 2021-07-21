import random as r  # import random module to generate new computer turns


class RPS:  # create class to ease variable assignment & instantiate game object

    def __init__(self, score=0):    # constructor for game object
        self.player2 = r.randint(0, 2)
        self.choice = ('rock', 'paper', 'scissors')
        self.player2 = self.choice[self.player2]
        self.bestof = int(0)
        self.bestofrange = (1, 2, 3, 4)
        self.score = score
        self.round = 0
        self.player1 = str('')
        self.start_game()

    def __str__(self):
        self.score_status()

    def redo(self):  # redo function to randomize player2 & prompt for new user input
        self.player2 = self.choice[r.randint(0, 2)]
        self.new_turn()

    def start_game(self):           # start_game function to initiate series length with exception handling

        try:
            self.bestof = int(input(
                'Please enter an integer between 1 and 4 to define x in this best-of-x rock, paper, scissors game: '))

            if self.bestof not in self.bestofrange:
                print('The value entered is not in the acceptable range.')
                self.start_game()

        except ValueError:
            print('The value entered was not an integer.')
            self.start_game()

        else:
            self.new_turn()

    def new_turn(self):             # new_turn function to initiate a new round of user input

        if self.round > 0:
            self.score_status()

        if -self.bestof < self.score < self.bestof:
            try:
                self.player1 = str.lower(input('Your turn. Please choose rock, paper or scissors: '))

                if self.player1 in self.choice:
                    self.get_score()

                elif self.player1 not in self.choice:
                    print("I'm sorry, that's not a valid choice.")
                    self.new_turn()

            except ValueError:
                print("I'm sorry, that's not a valid data type.")
                self.new_turn()

    def score_status(self):         # check if game is over, declare winner if so, status if not

        if self.score == self.bestof:
            print("    Score: Congratulations, you've won!")
            quit()

        elif self.score == -self.bestof:
            print("    Score: Dear Kind Sir, you've lost. Score: {} in a best-of {}".format(self.score, self.bestof))
            quit()

        elif -self.bestof < self.score < self.bestof:

            if self.score == 0:
                return '    Score: You are tied with player 2.\n'

            elif self.score > 0:
                return '    Score: You are up by {} in a best of {} series.\n'.format(self.score, self.bestof)

            elif self.score < 0:
                return '    Score: You are down by {} in a best of {} series.\n'.format(self.score, self.bestof)

    def get_score(self):            # update score after new inputs

        while True:
            self.round += 1

            self.score_status()

            if -self.bestof < self.score < self.bestof:

                if self.player1 == self.player2:
                    print('Round {} is a tie. {} {}...'.format(self.round, self.player1, self.player2))
                    self.redo()

                elif ((self.player1 == 'rock') and (self.player2 == 'paper')) or ((self.player1 == 'paper') and (self.player2 == 'scissors')) or ((self.player1 == 'scissors') and (self.player2 == 'rock')):
                    self.score -= 1
                    print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1,
                                                                                        self.player2))
                    print(self.score_status())
                    self.redo()

                elif ((self.player1 == 'scissors') & (self.player2 == 'paper')) or ((self.player1 == 'rock') and (self.player2 == 'scissors')) or ((self.player1 == 'paper') and (self.player2 == 'rock')):
                    self.score += 1
                    print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1,
                                                                                        self.player2))
                    print(self.score_status())
                    self.redo()


game = RPS()