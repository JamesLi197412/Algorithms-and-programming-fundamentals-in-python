def task1():
    # Task 1 Take as input from a file containing postcod/location information
    filename = input('Enter name of postcode file:')
    file_w = open(filename)
    L = []

    for eachline in file_w:
        eachline = eachline.expandtabs(2)  ##Replace the tab with space
        eachline = eachline.split(',')
        Number = int(eachline[0][0:4])
        # eachline=eachline[len(eachline)-1].strip('\n')
        for i in range(len(eachline)):
            if '\n' in eachline[i]:
                pp = eachline[i].split()
                # print(pp)
                postcode = pp[len(pp) - 1]
                # postcode=eachline[i].strip('\n')
                L.append([Number, postcode])
            elif i == 0:
                Letter = eachline[i][6:]
                L.append([Number, Letter])
            else:
                L.append([Number, eachline[i]])

    print(L)

def task2():
    ## Improve the readability
    filename = input('Enter name of postcode file:')
    file_w = open(filename)
    L = []
    def openfile(filename):
        for eachline in file_w:
            eachline = eachline.expandtabs(2)
            eachline = eachline.split(',')
            Number = int(eachline[0][0:4])
            # eachline=eachline[len(eachline)-1].strip('\n')
            for i in range(len(eachline)):
                if '\n' in eachline[i]:
                    pp = eachline[i].split()
                    # print(pp)
                    postcode = pp[len(pp) - 1]
                    # postcode=eachline[i].strip('\n')
                    L.append([Number, postcode])
                elif i == 0:
                    Letter = eachline[i][6:]
                    L.append([Number, Letter])
                else:
                    L.append([Number, eachline[i]])
        return L

    Openfile = openfile(filename)
    post = []

    for j in Openfile:
        print(j[0], ' ', j[1])
        post.append([j[0], j[1]])

def task3():
    # Taking information from file and sort the list in alphabetical order of location names

    filename = input('Enter name of postcode file:')
    file_w = open(filename)
    L = []

    def openfile(filename):
        for eachline in file_w:
            eachline = eachline.expandtabs(2)
            eachline = eachline.split(',')
            Number = int(eachline[0][0:4])
            # eachline=eachline[len(eachline)-1].strip('\n')
            for i in range(len(eachline)):
                if '\n' in eachline[i]:
                    pp = eachline[i].split()
                    # print(pp)
                    postcode = pp[len(pp) - 1]
                    # postcode=eachline[i].strip('\n')
                    L.append([Number, postcode])
                elif i == 0:
                    Letter = eachline[i][6:]
                    L.append([Number, Letter])
                else:
                    L.append([Number, eachline[i]])
        return L

    Openfile = openfile(filename)
    post = []

    # Gain min index
    def getMinIndex_alphabetical(mylist, start, stop):
        min_index = start
        for i in range(start + 1, stop):
            if mylist[i][1] < mylist[min_index][1]:
                min_index = i
        return min_index

    # Swap values
    def swapElements(mylist, i, j):
        temp = mylist[i]
        mylist[i] = mylist[j]
        mylist[j] = temp

    def sortinglist(Openfile):
        for i in range(len(Openfile)):
            min_index = getMinIndex_alphabetical(Openfile, i, len(Openfile))
            swapElements(Openfile, min_index, i)

        return Openfile

    sorted_Openfile = sortinglist(Openfile)

    for j in sorted_Openfile:
        print(j[0], ' ', j[1])

def task4():
    ## Use binary search to find Post code

    filename = input('Enter name of postcode file:')
    file_w = open(filename)
    L = []

    def openfile(filename):
        for eachline in file_w:
            eachline = eachline.expandtabs(2)
            eachline = eachline.split(',')
            Number = int(eachline[0][0:4])
            # eachline=eachline[len(eachline)-1].strip('\n')
            for i in range(len(eachline)):
                if '\n' in eachline[i]:
                    pp = eachline[i].split()
                    # print(pp)
                    postcode = pp[len(pp) - 1]
                    # postcode=eachline[i].strip('\n')
                    L.append([Number, postcode])
                elif i == 0:
                    Letter = eachline[i][6:]
                    L.append([Number, Letter])
                else:
                    L.append([Number, eachline[i]])
        return L

    Openfile = openfile(filename)
    post = []

    # Gain min index
    def getMinIndex_alphabetical(mylist, start, stop):
        min_index = start
        for i in range(start + 1, stop):
            if mylist[i][1] < mylist[min_index][1]:
                min_index = i
        return min_index

    # Swap values
    def swapElements(mylist, i, j):
        temp = mylist[i]
        mylist[i] = mylist[j]
        mylist[j] = temp

    def sortinglist(Openfile):
        for i in range(len(Openfile)):
            min_index = getMinIndex_alphabetical(Openfile, i, len(Openfile))
            swapElements(Openfile, min_index, i)

        return Openfile

    sorted_Openfile = sortinglist(Openfile)

    for j in sorted_Openfile:
        print(j[0], ' ', j[1])

    def binarySearch1(find, items):
        start = 0
        print(items)
        end = len(items)
        while start < end:

            mid = (start + end) // 2
            print(start, " ", mid, " ", end, "   ", find)
            if items[mid][1] == find:
                return mid
            elif items[mid][1] < find:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    Suburb_name = input('Enter Suburb Name:')

    mid = binarySearch1(Suburb_name, sorted_Openfile)
    if mid == -1:
        print('This Suburb did not exist in the file')
    else:
        print('Post code is ' + str(sorted_Openfile[mid][0]))


