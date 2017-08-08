def ex2():
    number = int(raw_input("Please enter a number: "))

    if number % 4 == 0:
        print "You have entered a multiple of 4"
    elif number % 2 == 0:
        print "You have entered an even number!"
    else:
        print "You have entered an odd number!"

    print "\nEnter 2 numbers - "
    num1 = int(raw_input("Enter first number: "))
    num2 = int(raw_input("Enter second number: "))

    if num1 % num2 == 0:
        print "The 2nd number is a factor of the 1st number"
    else:
        print "The 2nd number is not a factor of the 1st number"

ex2()