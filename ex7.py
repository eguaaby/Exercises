# One line of code to get even numbers
# from a list and put them in a new list
def ex7():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    evenNums = [number for number in a if number % 2 == 0]
    print evenNums

ex7()