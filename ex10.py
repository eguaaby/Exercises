# make a new list of common elements between 2 lists
# (without duplicates) using list comprehension

import random

def commonElements():
    # make 2 random lists
    list1 = random.sample(range(1, 100), 10)
    list2 = random.sample(range(1, 100), 15)
    print list1; print list2;

    if len(list1) < len(list2):
        listToPick = list1
        otherList = list2
    else:
        listToPick = list2
        otherList = list1

    # listToPick = [1, 1, 2, 3, 4, 2]
    # otherList = [1, 2, 1, 3, 3]

    commonList = []
    commonList = [comEl for comEl in listToPick if comEl in otherList]
    print; print commonList

commonElements()