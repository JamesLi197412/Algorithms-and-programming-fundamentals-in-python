
def task1(N,aList):
    ## N queens
    N = int(input('Please enter N:'))
    aList = []

    for i in range(N):
        Bosh = [0] * N
        aList.append(Bosh)

    for i in range(N):
        index = input('Enter position of Queen:')
        index = index.split()
        row_index = int(index[0])
        col_index = int(index[1])
        aList[row_index][col_index] = 1

    print(aList)


def task2(N,aList):
    ## N queens
    N = int(input('Please enter N:'))
    aList = []

    def printTable(alist):
        for i in range(len(alist)):
            for j in range(len(alist)):
                print(alist[i][j], end=' ')
            print()

    for i in range(N):
        Bosh = [0] * N
        aList.append(Bosh)

    for i in range(N):
        index = input('Enter position of Queen:')
        index = index.split()
        row_index = int(index[0])
        col_index = int(index[1])
        aList[row_index][col_index] = 1

    L = printTable(aList)


def task4(N,aList):
    ## N queens
    N = int(input('Please enter N:'))
    aList = []

    def printTable(alist):
        for i in range(len(alist)):
            for j in range(len(alist)):
                print(alist[i][j], end=' ')
            print()

    for i in range(N):
        Bosh = [0] * N
        aList.append(Bosh)

    L = []
    for i in range(N):
        index = input('Enter position of Queen:')
        index = index.split()
        row_index = int(index[0])
        col_index = int(index[1])
        aList[row_index][col_index] = 1
        L.append(row_index)

    print(L)

    K = printTable(aList)

def task5():
    ## N queens

    N = int(input('Please enter N:'))
    aList = []

    def printTable(alist):
        for i in range(len(alist)):
            for j in range(len(alist)):
                print(alist[i][j], end=' ')
            print()

    for i in range(N):
        Bosh = [0] * N
        aList.append(Bosh)

    L = []
    F_index = []

    for i in range(N):
        index = input('Enter position of Queen:')
        index = index.split()
        row_index = int(index[0])
        col_index = int(index[1])
        aList[row_index][col_index] = 1
        F_index.append([row_index, col_index])
        L.append(row_index)

    K = printTable(aList)

    # print(F_index)
    def checkSolution(F_index):
        print(F_index)
        for x in range(len(F_index)):
            for y in range(x, len(F_index)):

                if F_index[x][0] == F_index[y][0]:  # Checking rows
                    return False
                if F_index[x][1] == F_index[y][1]:  # Checking coloumns
                    return False
                if F_index[x][0] != F_index[y][0] and F_index[x][1] != F_index[y][1]:
                    run = (F_index[y][1] - F_index[x][1]) / (F_index[y][0] - F_index[x][0])

                    if run == -1 or run == 1:
                        return False

    ####        run=(int(F_index[y][1])-int(F_index[x][1]))(int(F_index[y][0])-int(F_index[x][0]))
    ##        if F_index[x][0]==F_index[y][0]:
    ##                return False
    ##            elif F_index[x][1]==F_index[y][1]:
    ##                return False
    ##            elif run==1 or run ==-1 or run==0:
    ##                return False

    def printresult(Q):
        if Q == False:
            print('This is not a real solution to the problem')
        else:
            print('This is a real solution to the problem')

    Q = checkSolution(F_index)

    K = printresult(Q)
