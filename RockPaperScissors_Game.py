import random as r      #import random module to generate new computer turns

class RPS:              #create class to ease variable assignment & object instatiation

    def __init__(self, score = 0):
        self.player2 = r.randint(0,2)   #set up player2 variable range based on self.choice index range
        self.choice = ('rock', 'paper', 'scissors') #define viable user inputs for each turn
        self.player2 = self.choice[self.player2]    #defines player2 as random choicec from self.choice
        self.bestof = int(0)            #defines new blank variable for bestof series
        self.bestofrange = (1,2,3,4)    #defines acceptable range for bestof series, immutable & ordered
        self.score = score              #defines score counter with starting value of zero
        self.round = 0                  #defines round counter with starting value of zero
        self.player1 = str('')          #defines player1 input as blank string, to be provided by user
        self.start_game()               #initiates start_game function to prompt user inputs

    def __str__(self):                  #string dunder method to show status if called
        self.score_status()
        

    def redo(self):                     #redo function to randomize player2 & prompt for new user input
        self.player2 = self.choice[r.randint(0, 2)]
        self.new_turn()
        
        
    def start_game(self):               #start_game function to initiate series lenght with exception handling

        try:
            self.bestof = int(input('Please enter an integer between 1 and 4 to define x in this best-of-x rock, paper, scissors game: '))

            if self.bestof not in self.bestofrange:
                print('The value entered is not in the acceptable range.')
                self.start_game()        

        except ValueError:
            print('The value entered was not an integer.')
            self.start_game()

        else:
            self.start_game_part_two()
            

    def start_game_part_two(self):      #start_game_part_two function to initiate first round of user input

        try:
            self.player1 = str.lower(input('Please choose rock, paper or scissors: '))

            if self.player1 in self.choice:
                self.get_score()

            elif self.player1 not in self.choice:
                print("I'm sorry, that's not a valid choice.")
                self.start_game_part_two()

        except ValueError:
            print("I'm sorry, that's not a valid data type.")
            self.start_game_part_two()
            

    def score_status(self):             

        if self.score == self.bestof:
                print("    Score: Congratulations, you've won!")
                quit()

        elif self.score == -self.bestof:
                print("    Score: Dear Kind Sir, you've lost")
                quit()

        elif self.score > -self.bestof and self.score < self.bestof:

            if self.score == 0:
                return '    Score: You are tied with player 2.\n'

            elif self.score > 0:
                return '    Score: You are up by {} in a best of {} series.\n'.format(self.score, self.bestof)

            elif self.score < 0:
                return '    Score: You are down by {} in a best of {} series.\n'.format(self.score, self.bestof)


    def new_turn(self):

        if self.score == self.bestof:
            print("    Score: Congratulations, you've won!")
            quit()

        elif self.score == -self.bestof:
            print("    Score: Dear Kind Sir, you've lost")
            quit()

        elif self.score >= -self.bestof and self.score <= self.bestof:
            self.player1 = str.lower(input('Your turn. Please choose rock, paper or scissors: '))

            if self.player1 in self.choice:
                self.get_score()

            else:
                print("I'm sorry that's not a valid choice.")
                self.new_turn()


    def get_score(self):

        while True:
            self.round += 1

            if self.score == self.bestof:
                print("    Score: Congratulations, you've won!")
                quit()

            elif self.score == -self.bestof:
                print("    Score: Dear Kind Sir, you've lost.")
                quit()

            elif self.score > -self.bestof and self.score < self.bestof:

                if self.player1 == self.player2:
                    print('Round {} is a tie. {} {}...'.format(self.round, self.player1, self.player2))
                    self.redo()

                elif self.player1 == 'rock':

                    if self.player2 == 'paper':
                        self.score -= 1
                        print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1, self.player2))
                        print(self.score_status())
                        self.redo()

                    elif self.player2 == 'scissors':
                        self.score += 1
                        print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1, self.player2))
                        print(self.score_status())
                        self.redo()

                elif self.player1 == 'paper':

                    if self.player2 == 'scissors':
                        self.score -= 1
                        print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1, self.player2))
                        print(self.score_status())
                        self.redo()

                    elif self.player2 == 'rock':
                        self.score += 1
                        print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1, self.player2))
                        print(self.score_status())
                        self.redo()

                elif self.player1 == 'scissors':

                    if self.player2 == 'paper':
                        self.score += 1
                        print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1, self.player2))
                        print(self.score_status())
                        self.redo()

                    elif self.player2 == 'rock':
                        self.score -= 1
                        print('\nRound {} results: \n    You: {} \n    Player 2: {}'.format(self.round, self.player1, self.player2))
                        print(self.score_status())
                        self.redo()

game = RPS()
