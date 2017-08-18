# user tells how long of a
# Fibonnaci series they want

def makeFibonnaci():
    lengthOfSeries = getLength()
    fibonacciSeries = []
    firstNum = 1
    secondNum = 1
    nextNum = 0
    if lengthOfSeries == 1:
        fibonacciSeries = [firstNum]
        print fibonacciSeries

    elif lengthOfSeries == 2:
        fibonacciSeries = [firstNum, secondNum]
        print fibonacciSeries

    elif lengthOfSeries > 2:
        fibonacciSeries = [firstNum, secondNum]
        for i in range(lengthOfSeries-2):
            nextNum = firstNum + secondNum
            fibonacciSeries.append(nextNum)
            firstNum = secondNum
            secondNum = nextNum
        print fibonacciSeries

    else:
        print "The length of the series has to be at least 1!"


def getLength(message="How long of a Fibonnaci series do you want: "):
    return int(raw_input(message))

# def test():
#     for i in range(3):
#         print i

# test()
makeFibonnaci()