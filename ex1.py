import datetime
import sys

def ex1():
    name = raw_input("Hi! What is your name? ")
    age = int(raw_input("What is your age? "))
    # obtain an object which contains all time details. these
    # are accessible by now.year, now.month, now.hour, now.day etc
    now = datetime.datetime.now()
    answer = now.year + (100-age)
    message = "Hi " + name + ", you will be 100 years old in the year " + str(answer)
    print message
    number = int(raw_input("Enter a number between 1 and 10: "))
    if number < 1 or number > 10:
        print "Please enter a number between 1 and 10!\nProgram exiting"
        sys.exit(1)

    for i in range(0, number):
        print message

def test():
    now = datetime.datetime.now()
    print now.year
    print(4 * "test")

ex1()