# Check whether the input string
# is a palindrome or not
def ex6():
    user_input = raw_input("Please enter a word: ")
    palindrome = True
    wordLength = len(user_input)
    for i in range(0, wordLength/2 + 1):
        if user_input[i] != user_input[wordLength-1-i]:
            palindrome = False

    if palindrome:
        print "The word is a palindrome!!"
    else:
        print "The word is not a palindrome"

ex6()