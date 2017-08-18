# reverse the string/sentence
# entered by the user

def reverseString():
    string = raw_input("Please enter a sentence: ")
    listOfWords = string.split()
    length = len(listOfWords)
    reversedString = ""
    for i in range(length):
        reversedString += listOfWords[length - 1 - i] + " "

    print reversedString

reverseString()