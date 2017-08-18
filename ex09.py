# user guesses number between 1 and 9
# tell if too low, high or exactly right

from random import *

def numberGuessing():
    numberToGuess = randint(1,9)
    numberOfGuesses = 0
    guess = ""
    run = True
    while run:
        guess = raw_input("\nGuess the number between 1 and 9: ")
        if guess == "exit":
            break
        userGuess = int(guess)
        numberOfGuesses += 1
        if userGuess < numberToGuess:
            print "The guess is too low!"
        elif userGuess > numberToGuess:
            print "The guess is too high!"
        else:
            print "Yay! You guessed it right!"
            print "It took you", numberOfGuesses, "guesses to get it right"
            run = False

numberGuessing()