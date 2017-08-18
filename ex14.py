# take a list, remove duplicates
# in it and return a new list

import random

a = [1, 2, 5, 2, 7, 8, 1, 8, 3, 3, 5, 4, 6]

def removeDuplicatesUsingSets():
    print list(set(a))

def removeDuplicatesUsingLists():
    listWithoutDuplicates = []
    for i in a:
        if i not in listWithoutDuplicates:
            listWithoutDuplicates.append(i)

    print listWithoutDuplicates

removeDuplicatesUsingLists()