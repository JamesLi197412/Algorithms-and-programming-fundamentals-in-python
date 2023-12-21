## Purpose: This file is designed to computes an approximation for the
##          value of e using the n+1 terms of continued fraction
## Last Modified :5/09/2018
n = input('Please give non-negative integer:')


# To calculate approximation for value of e
def continuedFraction(n):
    # User input value
    n_int = int(n)

    # Checking interger invaild or not
    if n_int > 0:
        pass
    else:
        while n_int < 0:
            n_int = int(input('Please give an non-negative integer:'))

    # Beginning n+1 terms of continued fraction to gain approximation
    n_after1 = n_int + 1;
    for i in range(n_int, 0, -1):
        fraction = i / n_after1
        sum_fraction = i + fraction
        n_after1 = sum_fraction

    e = 2 + 1 / n_after1;

    print('The approxiamted e value is:', e)


# Call the function
continuedFraction(n)


# Assignment Part II

## Assignment 2 Part II magic squares
## Purpose: This file is designed to check whether the square is always a
##          Magic Square

## Last Modified :6/09/2018

# Global Variables
filename = input('Please input the file name:')
a = 0


# This function is used to read the file
def readFile(filename):
    file_r = open(filename)
    L = [];
    for eachline in file_r:
        if (len(eachline) != 1 and eachline[0] != 'M'):
            # Call function to transfer str to int
            Eachline = strToInt(eachline)
            L.append(Eachline)
        if eachline[0] == 'M':
            magicSum = int(eachline[10:])

    return L, magicSum


# This function is used to calculate the sum of rows
def sumRow(L, row):
    mysum = 0
    for i in range(len(L)):
        mysum += L[row][i]
    return mysum


# This function is used to calculate the sum of coloumn
def sumCol(L, col):
    mysum = 0
    for i in range(len(L)):
        mysum += L[i][col]
    return mysum


# This function is used to tranform string into int
def strToInt(line):
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    return line


# Present the table
def presentTable(L):
    for i in range(len(L)):
        for j in range(len(L)):
            print(L[i][j], end=' ')

        print()


## This function is used to check whether there is any cell inisde the table
def checkingTableCell(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j] == 0:
                return True


# This function is used to check the sum of table vaild or not
def checkingTable_Sum(L, magicSum):
    # Checking the sum of rows
    for i in range(len(L)):
        if sumRow(L, i) > magicSum:
            return False

    # Checking the sum of coloumns
    for i in range(len(L)):
        if sumCol(L, i) > magicSum:
            return False

    # Checking 2 main diagonal
    sumdiagonal_1 = 0
    sumdiagonal_2 = 0
    for i in range(len(L)):
        sumdiagonal_1 = sumdiagonal_1 + L[i][i]
        sumdiagonal_2 = sumdiagonal_2 + L[len(L) - i - 1][i]

    if sumdiagonal_1 > magicSum or sumdiagonal_2 > magicSum:
        return False


# This function is used to check whether there is any repeated value
def checkingValue(L, num_value, row_ind, col_ind):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j] == num_value and i != row_ind and j != col_ind:
                return False


# Checking the index invaild or not
def checkingIndex(row_ind, col_ind, L):
    if row_ind > len(L) or col_ind > len(L):
        return False


# This function is used to input number into index user input

def inputCell(L, magicSum):
    # Ask user to input cell index and value
    row_ind = int(input('Enter the row index:'))
    col_ind = int(input('Enter the coloumn index:'))
    num_value = int(input('Enter the numerical value:'))

    if checkingIndex(row_ind, col_ind, L) == False:
        print('Please input the reasonable index')
        row_ind = int(input('Enter the row index:'))
        col_ind = int(input('Enter the coloumn index:'))

    # Checking whether the cell is vaild or not
    if L[row_ind][col_ind] != 0:
        print('This is an invalid entry')
        # Stop function
        return
    else:
        L[row_ind][col_ind] = num_value

    if checkingTable_Sum(L, magicSum) == False:
        print('It is against the magic Square properties')
        L[row_ind][col_ind] = 0
    else:
        print('Vaild')

    if checkingValue(L, num_value, row_ind, col_ind) == False:
        print('This value has already exists and choose another one')


# Checking the original file whether there is any cell in table
alist = []


def checkingValues(L):
    for i in range(len(L)):
        for j in range(len(L)):
            alist.append(L[i][j])

    for a in range(len(alist)):
        if alist[a] != 0:
            for b in range(a + 1, len(alist)):
                if alist[a] == alist[b]:
                    return False


# Call function to read file
L, magicSum = readFile(filename)

# Checking the original file & Only checking once
if checkingValues(L) == False:
    print('Values are repeated in original input,Thus It is not a magic square!!!')
    a = 'False'
if checkingTable_Sum(L, magicSum) == False:
    a = 'False'
    print('The Sum of some rows,coloumns or main diagonal>Sum Magic Square => it is not a Magic Suqare')

while True:
    if a == 'False':
        break

    # Check cell
    if checkingTableCell(L) != True:
        # Check Sum
        if checkingTable_Sum(L, magicSum) != False:
            print('The Square is done and is a Magic Square')
        else:
            presentTable(L)
            print('There is no more cell in this square')
            print('This is not a Magic Suqre & against the properties of Sum')
        break

    decision = input('Do you wish to contiune(y=Yes;n=No):')

    while decision != 'n' and decision != 'y':
        decision = input('Please only choose the y OR n(y=Yes;n=No):')

    if decision == 'n':
        break

    presentTable(L)

    inputCell(L, magicSum)

    presentTable(L)


















