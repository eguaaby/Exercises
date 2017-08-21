# generate a random weak
# or strong password

import random
import string

def generateRandomPassword(charsChosen, size):
    listOfChars = random.sample(charsChosen, size)
    pwd = ''.join(listOfChars)
    print pwd

def main():
    howStrong = raw_input("Do you want a weak password or a strong password? ")
    howLong = int(raw_input("How many characters do you want the password to be? "))
    if howStrong == "strong":
        # 'string.printable' gives all
        # possible printable characters
        allChars = list(string.printable)
        # removing unwanted characters
        allChars.remove('\n'); allChars.remove('\t'); allChars.remove('\r'); allChars.remove('\x0b'); allChars.remove('\x0c')
        allChars.remove('\\'); allChars.remove(' '); allChars.remove('`')
        generateRandomPassword(allChars, howLong)

    elif howStrong == "weak":
        # 'string.ascii_letters' gives all
        # the alphabets, lowercase + uppercase
        weakChars = string.ascii_letters
        generateRandomPassword(weakChars, howLong)

main()