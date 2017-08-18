# ask user for a number and check
# whether it is prime or not

def prime_or_not():
    number = get_number()

    # Special cases
    if number == 1:
        isPrime = False
    elif number == 2:
        isPrime = True

    else:
        isPrime = True
        for i in range(2, number/2 + 1):
            if number % i == 0:
                isPrime = False
                break

    print_result(isPrime)

def print_result(isPrime):
    if isPrime:
        print "The number is prime!"
    else:
        print "The number is not prime"


def get_number(message="Please input a number: "):
    return int(raw_input(message))


prime_or_not()