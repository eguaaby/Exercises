from random import *

def ex5():
    # common=[]
    # c=[]
    # if len(a) < len(b):
    #     c = a
    # else:
    #     c = b
    # for num in c:
    #     if num in a and num in b:
    #         common.append(num)

    # print common

    # finding common numbers for given lists a and b
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    commonNums = set(a).intersection(set(b))
    print "For given lists:"
    print a; print b; print; print list(commonNums)
    print

    # finding common numbers for randomly generated lists
    list1=[]; list2=[]
    for i in range(1,11):
        list1.append(randint(1,100))

    for i in range(1,16):
        list2.append(randint(1,100))

    print "For generated lists:"
    print list1; print list2; print
    commonNumbersRandomLists = set(list1).intersection(set(list2))
    print list(commonNumbersRandomLists)

ex5()