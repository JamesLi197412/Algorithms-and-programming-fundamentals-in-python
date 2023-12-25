def task1():
    ## Task 1_Task A

    def printTable(alist):
        for i in range(len(alist)):
            for j in alist[i]:
                print(j, end=' ')
            print()

    def getPositions(queenList, n):
        #   This function returns a list of possible position for the next queen

        #   This populates the answer array
        possiblePositions = []

        for index in range(0, n):
            possiblePositions.append(index)

        #   This removes the elements in the same rows as queens currently placed
        for index in queenList:
            possiblePositions.remove(index)

        partialSolSize = len(queenList)
        elementsToRemove = []

        # The following nested loops store the elements that need to be removed

        for row in range(0, partialSolSize):
            for col in range(0, len(possiblePositions)):
                rowDifference = abs(queenList[row] - possiblePositions[col])
                colDifference = abs(row - partialSolSize)
                if rowDifference == colDifference:
                    elementsToRemove.append(possiblePositions[col])

        # This remove the diagonally conflicting elements
        for index in elementsToRemove:
            if index in possiblePositions:
                possiblePositions.remove(index)

        # The following prints chessboard
        chessboard = n * [0]
        for index in range(0, n):
            chessboard[index] = n * [0]

        for index in range(0, len(queenList)):
            chessboard[queenList[index]] = 'Q'

        for index in range(0, len(possiblePositions)):
            chessboard[possiblePositions[index]][partialSolSize] = 'X'

        return chessboard

    chessboard = getPositions([5, 3], 6)
    printTable(chessboard)



def task2():
    ## Task 2: Implementing Backtracking
    def nQueens(partialSolution, n, countArray):
        positions = getPositions(partialSolution, n)

        if positions == []:
            if len(partialSolution) == n:
                print(partialSolution)
                countArray.append(0)

        else:
            for element in positions:
                partialSolution.append(element)  # Push element into partialSolution
                nQueens(partialSolution, n, countArray)
                partialSolution.pop()

    def getPositions(queenList, n):
        # This function returns a list of possible positions for the next queen

        #   This populates the answer array
        possiblePosition = []
        for index in range(0, n):
            possiblePosition.append(index)

        #   This removes the elements in the same  rows as qeens currently placed
        for index in queenList:
            possiblePosition.remove(index)

        partialSolSize = len(queenList)
        elementsToRemove = []

        # The following nested loops store the elements that need to be removed due to diagonally
        for row in range(0, partialSolSize):
            for col in range(0, len(possiblePosition)):
                rowDifference = abs(queenList[row] - possiblePosition[col])
                colDifference = abs(row - partialSolSize)
                if rowDifference == colDifference:
                    elementsToRemove.append(possiblePosition[col])

        # This removes the diagonally conflicting elements
        for inde in elementsToRemove:
            if index in possiblePosition:
                possiblePosition.remove(index)

        return possiblePosition

    n = int(input(' Enter value for n : '))
    solution = []

    print('-------------------------')
    nQueens([], n, solution)

    print('-----------------------------')
    if len(solution) == 0:
        print('No solution')
    else:
        print('There are', len(solution), 'Solution')

def task3():
    ## N-Queens brute forced!

    def isSolution(queensList, size):
        #   The following nested loops store the elements that need to be removed due to diagonal
        if not len(queensList) == size:
            return False  # Pedanti, should not occur

        for col in range(0, size):
            for otherCol in range(col + 1, size):
                rowDifference = abs(queensList[col] - queensList[otherCol])
                colDifference = abs(col - otherCol)

                #   Horizontal distance mathces vertical distance

                if rowDifference == colDifference:
                    return False

                if queensList[col] == queensList[otherCol]:
                    return False  # duplicate found ,same row

        return True

    def allPerms(numList):
        return allPermutes(numList, [], [])

    # permutations by backtracking for convenience

    def allPermutes(numList, partial, allList):
        if len(partial) == len(numList):
            allList.append(partial[:])

        else:
            for item in numList:
                if not item in partial:
                    partial.append(item)
                    allPermutes(numList, partial, allList)
                    partial.pop()

    #   Now the brute force

    def bruteNQueen(size):
        valid_solutions = []

        nums = []

        for i in range(size):
            nums.append(i)

        perms = allPerms(nums)

        for perm in perms:
            if isSolution(perm, size):
                valid_solutions.append(perm)

        return valid_solutions

    N = int(input('Please enter the size of N: '))

    print('Number of solutions :', len(bruteNQueen(N)))

