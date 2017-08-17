# Rock Paper Scissors
# for 2 players
def ex8():
    # scores for players
    player1_score = 0
    player2_score = 0

    quit_message = "Thanks for playing!"

    # dictionary storing players' info
    playersDictionary = {
        'P1':{'message': "Player 1 wins!", 'score': 0},
        'P2':{'message': "Player 2 wins!", 'score': 0},
        'NA':{'message': "It's a tie!", 'score': 0}
    }

    # bool condition to play game
    playMore = True
    while playMore:
        print "\nRock Paper Scissors: The moves are 'rock', 'paper', 'scissors'"
        player1_move = raw_input("Enter move for player 1: ")
        player2_move = raw_input("Enter move for player 2: ")

        # if either of the players enters 'quit',
        # we display the score and exit the game
        if player1_move == "quit" or player2_move == "quit":
            print "The score was: ", playersDictionary['P1']['score'], "-", playersDictionary['P2']['score']
            print quit_message
            break

        player1_move_index = parseMove(player1_move)
        player2_move_index = parseMove(player2_move)

        # the matrix is designed like this -
        #   P1\P2     Rock    Paper   Scissors
        #   Rock       NA         P2      P1
        #   Paper      P1         NA      P2
        #   Scissors   P2         P1      NA
        #
        # The result is 1 if player1 wins and
        # -1 if player2 wins. It's 0 for a tie
        matrix = [['NA', 'P2', 'P1'], ['P1', 'NA', 'P2'], ['P2', 'P1', 'NA']]

        # index into the matrix and get the outcome
        outcome = matrix[player1_move_index][player2_move_index]
        winner=playersDictionary[outcome]
        print winner['message']
        winner['score'] += 1

        moreGames = raw_input("\nDo you want to start a new game? ")
        if moreGames == "yes":
            playMore = True
        elif moreGames == "no":
            print "The score was: ", playersDictionary['P1']['score'], "-", playersDictionary['P2']['score']
            print quit_message
            playMore = False


# translate the (string) moves
# to index values for the matrix
def parseMove(player_move):
    # index value for 'rock' is 0
    move_equivalent_index = 0
    if player_move == "paper":
        move_equivalent_index = 1
    elif player_move == "scissors":
        move_equivalent_index = 2

    return move_equivalent_index

ex8()