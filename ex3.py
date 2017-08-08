def ex3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for element in a:
        if element < 5:
            print element
    print

    lessthanfive = []
    for element in a:
        if element < 5:
            lessthanfive.append(element)

    print lessthanfive
    print

    lessthannum = []
    num = int(raw_input("Please enter a number: "))
    for element in a:
        if element < num:
            lessthannum.append(element)

    print lessthannum

ex3()