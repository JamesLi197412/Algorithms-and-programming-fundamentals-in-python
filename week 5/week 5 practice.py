"""
findRoot function will, given an appropriate expression and upper and l bound will return a valid root for a given expression (where the expression intersects the X axis)
@param: expression - an expression in terms of X in python form (eg. X**2 for X squared). Note the case is important here
@param: l - the left end of the range to search through
@param: u - the right end of the range to search through
"""
def findRoot(e, l, u):
    def re(e, t):
        X = t
        return eval(e)
    t = 1e-8
    xm=((l + u) / 2)
    if ((l - u)**2) < t:
        return xm
    else:
        yl = re(e, l)
        ym = re(e, xm)
        yu = re(e, u)
        s = lambda b: 1 if b > 0 else -1 if b < 0 else 0
        if s(ym) == 0:
            return xm
        elif s(yl) == s(yu):
            raise ValueError("no root in range")
        else:
            if s(yl) != s(ym):
                return findRoot(e, l, xm)
            else:
                return findRoot(e, xm, u)


def task1():
    # Task 1
    filename = input('Enter name of file: ')
    readFromFile = open(filename)
    List = []

    for line in readFromFile:
        line = line.split(',')
        if len(line) != 1:
            List.append(line)

    for element in List:
        element[0] = int(element[0])
        element[1] = element[1].strip()
        element[1] = float(element[1])

    # Improving Readability
    for element in List:
        print(str(element[0]), 'kms, $', str(element[1]))

def task2():
    # Task 2 :Sort list by Distance
    filename = input('Enter name of file: ')
    readFromFile = open(filename)
    List = []

    for line in readFromFile:
        line = line.split(',')
        if len(line) != 1:
            List.append(line)

    for element in List:
        element[0] = int(element[0])
        element[1] = element[1].strip()
        element[1] = float(element[1])

    # Swapping the values
    def swapping(myList, i, j):
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp

    # Implementing Selection Sort
    def getMinIndex(myList, start, stop):
        min_index = start
        for i in range(start + 1, stop):
            if myList[i] < myList[min_index]:
                min_index = i
        return min_index

    # Arrange List in the increasing order of distance
    def selectionSortDistance(List):
        n = len(List)
        for index in range(n):
            # Find position of smallest number in alist[index:]
            min_position = getMinIndex(List, [index][0], n)

            # Swap numbers at index and min-position
            swapping(List, [index][0], min_position)

        return List

    List = selectionSortDistance(List)
    print(List)
    # Improving Readability
    for element in List:
        print(str(element[0]), 'kms, $', str(element[1]))


def task3():
    # Task 3 : Sort it by price

    filename = input('Enter name of file: ')
    readFromFile = open(filename)
    List = []

    for line in readFromFile:
        line = line.split(',')
        if len(line) != 1:
            List.append(line)

    for element in List:
        element[0] = int(element[0])
        element[1] = element[1].strip()
        element[1] = float(element[1])

    # Swapping the values
    def swapping(myList, i, j):
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp

    # Implementing Selection Sort
    def getMinIndex(myList, start, stop):
        min_index = start
        for i in range(start + 1, stop):
            if myList[i][1] < myList[min_index][1]:
                min_index = i
        return min_index

    # Arrange List in the increasing order of distance
    def selectionSortPrice(List):
        n = len(List)
        for index in range(n):
            # Find position of smallest number in alist[index:]
            min_position = getMinIndex(List, index, n)

            # Swap numbers at index and min-position
            swapping(List, index, min_position)

        return List

    List = selectionSortPrice(List)

    # Improving Readability
    for element in List:
        print(str(element[0]), 'kms, $', str(element[1]))

def task4():
    # Task 4: Sort it by choices

    filename = input('Enter name of file: ')
    readFromFile = open(filename)
    List = []
    Choice = input('Enter choice of Print, Sort1(distance),Sort2(price) or Quit: Print')

    for line in readFromFile:
        line = line.split(',')
        if len(line) != 1:
            List.append(line)

    for element in List:
        element[0] = int(element[0])
        element[1] = element[1].strip()
        element[1] = float(element[1])

    # Swapping the values
    def swapping_price(myList, i, j):
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp

    # Implementing Selection Sort
    def getMinIndex_price(myList, start, stop):
        min_index = start
        for i in range(start + 1, stop):
            if myList[i][1] < myList[min_index][1]:
                min_index = i
        return min_index

    # Arrange List in the increasing order of distance
    def selectionSortPrice(List):
        n = len(List)
        for index in range(n):
            # Find position of smallest number in alist[index:]
            min_position = getMinIndex(_priceList, index, n)

            # Swap numbers at index and min-position
            swapping_price(List, index, min_position)

        return List

    # Swapping the values
    def swapping(myList, i, j):
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp

    # Implementing Selection Sort
    def getMinIndex(myList, start, stop):
        min_index = start
        for i in range(start + 1, stop):
            if myList[i] < myList[min_index]:
                min_index = i
        return min_index

    # Arrange List in the increasing order of distance
    def selectionSortDistance(List):
        n = len(List)
        for index in range(n):
            # Find position of smallest number in alist[index:]
            min_position = getMinIndex(List, [index][0], n)

            # Swap numbers at index and min-position
            swapping(List, [index][0], min_position)

        return List

    List = selectionSortPrice(List)

    while Choice != 'Quit':
        if (Choice == 'Print'):
            # Improving Readability
            for element in List:
                print(str(element[0]), 'kms, $', str(element[1]))

        elif (Choice == 'Sort1'):
            List = selectionSortDistance(List)
            # Improving Readability
            for element in List:
                print(str(element[0]), 'kms, $', str(element[1]))

        elif (Choice == 'Sort2'):
            List = selectionSortPrice(List)
            # Improving Readability
            for element in List:
                print(str(element[0]), 'kms, $', str(element[1]))


