# RPS
Rock, Paper, Scissors Game for python IDEs

The .py file can be run via IDE. Initial prompt is for the user to declare x in a best-of-x series format. Once the series is defined, the user will be prompted to choose rock, paper or scissors. Each round of RPS will trigger the printing of a readout of the round number, player choices and the game score. Once the game is completed the score will show the winner and the game will quit.

Error handling is in place to manage series inputs as integers between 1 and 4, as well as turn choices within the tuple ('rock', 'paper', 'scissors'). Going outside those ranges will trigger a corrective warning and a renewed prompt to choose among the available options.

The opponent is a randomly generated selection that is refreshed before each round of play. As there are only three choices in the gameplay, ties frequently occur. 
