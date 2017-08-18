# Print a list of divisors
# of the input number
def ex4():
    divisors = []
    number = int(raw_input("Please enter a number: "))
    divisors.append(1)
    for i in range(2, number/2 + 1):
        if number % i == 0:
            # i divides 'number' without
            # any remainder. therefore
            # it is a factor of 'number'
            divisors.append(i)

    divisors.append(number)
    print divisors,
    print "- %d divisors" % len(divisors)

def test():
    # make a list of numbers from 1-10
    # **************************
    x = range(1,11)
    # **************************
    print x

ex4()