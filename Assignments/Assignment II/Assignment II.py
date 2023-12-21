## Student ID: 28280016
## Full Name: Zhiyue Li
## Last Modified: 28/09/2018

## Purpose :This file is designed to allow user to input a non-gative
##          integer N and prints out the first n+1 rows of Pascal's triangle

##--------------------------------------------------

import math

#Global variables
L=[]
N=int(input('Enter N:'))


## Checking the vaild N
while N <0:
    N=int(input('Please enter non-negative N:'))

# This function used to calculate each element in the row

def creatingline(row_list,N):
    # counting elements from 0-len(row)
    for i in range(N+1):
        # Combination formula
        element=math.factorial(N)/math.factorial(N-i)/math.factorial(i)
        row_list.append(int(element))
    return row_list

# This function used to print each row

def printRow(row_list):
    for i in range(len(row_list)):
        print(row_list[i],end=' ')
    print()


# This function is prints out the first n + 1 rows of Pascal's triangle.

def printPascal(L,N):
    if N==0:
        print(1)
    else:
        printPascal(L,N-1)
        row_list=[]
        row_list=creatingline(row_list,N)
        printRow(row_list)



# Call function
printPascal(L,N)

## Student ID: 28280016
## Full Name: Zhiyue Li
## Last Modified: 10/10/2018

# Purpose : The program should then display a menu that allows the user to
#           sort the list by different attributes of the CDs or search for CDs based
#           on these attributes until the user elects to quit.

##------------------------------

# Global Variables
filename = input('Enter the filename:')
file_r = open(filename, 'r+')
aList = []
Find = []


# This function used to organise information in file
def createDatabase():
    for line in file_r:
        eachline = line.strip('\n')

        eachline = eachline.split(',')
        aList.append(eachline)
    return aList


# This function is used to transfer str to number
def str2int(aList):
    for lists in aList:
        # each element's len is 4
        lists[3] = float(lists[3])
    return aList


aList = createDatabase()
aList = str2int(aList)


# -----------------------------------------------
# Sorting by Title
# Gain min index
def getMinIndex_Title(mylist, start, stop):
    min_index = start
    for i in range(start + 1, stop):
        if mylist[i][0] < mylist[min_index][0]:
            min_index = i
    return min_index


# Swap values
def swapElements(mylist, i, j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp


# Function used to sort list by title
def SortByTitle(aList):
    for i in range(len(aList)):
        min_index = getMinIndex_Title(aList, i, len(aList))
        swapElements(aList, min_index, i)

    return aList


# ------------------------------------------------------------


# Print the list
def PrintList(aList_title):
    for eachlist in aList_title:
        print('Title: ' + eachlist[0])
        print('Artist: ' + eachlist[1])
        print('Genre: ' + eachlist[2])
        print('Price: $ ' + str(eachlist[3]))
        print('-------------------------------------------------')
        # print("%10s %4s %12s %12s" % (data[0],data[1],data[2], str(data[3])))


# ----------------------------------------------------------
# Sorting by Genre
# Gain min index
def getMinIndex_Genre(mylist, start, stop):
    min_index = start
    for i in range(start + 1, stop):
        if mylist[i][2] < mylist[min_index][2]:
            min_index = i
    return min_index


# Function used to sort list by Genre
def SortByGenre(aList):
    for i in range(len(aList)):
        min_index = getMinIndex_Genre(aList, i, len(aList))
        swapElements(aList, min_index, i)

    return aList


# -------------------------------------------------------
# Gain min index for artist
def getMinIndex_Artist(mylist, start, stop):
    min_index = start
    for i in range(start + 1, stop):
        if mylist[i][1] < mylist[min_index][1]:
            min_index = i
    return min_index


# Function used to sort list by Artist
def SortByArtist(aList):
    for i in range(len(aList)):
        min_index = getMinIndex_Artist(aList, i, len(aList))
        swapElements(aList, min_index, i)

    return aList


# ---------------------------------------------------


# ------------------------------------------------
# Sorting by price

# getMinIndex_Price
def getMinIndex_Price(mylist, start, stop):
    min_index = start
    for i in range(start + 1, stop):
        if mylist[i][3] < mylist[min_index][3]:
            min_index = i
    return min_index


# Sorting by price
def SortByPrice(aList):
    for i in range(len(aList)):
        min_index = getMinIndex_Price(aList, i, len(aList))
        swapElements(aList, min_index, i)

    return aList


# ------------------------------------------------------
## This function is used to find appropriate price and
def FindByPrice(aList, Price):
    ##Sot the list by price first
    aList_Price = SortByPrice(aList)

    ## Using the Brute Force to find
    for eachCD in aList_Price:

        if eachCD[3] <= Price:
            Find.append(eachCD)

    return Find


# -------------------------------------------------

# Find by Artist
def FindByArtist(Artist, aList):
    ## Using the Brute Force to find
    for eachCD in aList:
        if eachCD[1] == Artist:
            Find.append(eachCD)

    return Find


# ------------------------------------------------

# Find by Title
def FindByTitle(Title, aList):
    ## Using the Brute Force to find
    for eachCD in aList:
        if eachCD[0] == Title:
            Find.append(eachCD)

    return Find


# ----------------------------------------------
# Find by Genre
def FindByGenre(alist, Genre):
    ## Using the Brute Force to find
    for eachCD in alist:
        if eachCD[2] == Genre:
            Find.append(eachCD)

    return Find


# ----------------------------------------------

def DisplayMenu():
    print('1. Print List of CDs')
    print('2. Sort CDs by Title')
    print('3. Sort CDs by Artist')
    print('4. Sort CDS by Genre')
    print('5. Sort CDs by Price')
    print('6. Find All CDs by Title')
    print('7. Find All CDs by Artist')
    print('8. Find All CDs by Genre')
    print('9. Find All CDs with Price at Most Price X')
    print('10. Quit')


# Display the menu
A = DisplayMenu()
Option = int(input('Which option would you like:'))

while Option < 1 or Option > 10:
    Option = int(input('Please enter option between 1 and 10:'))


def decision(Option, aList):
    # Print List of CDs
    if Option == 1:
        PrintList(aList)

    #  Sort CDs by Title
    if Option == 2:
        alist_Title = SortByTitle(aList)
        PrintList(alist_Title)

    # Sort CDs by Artist
    if Option == 3:
        alist_Artist = SortByArtist(aList)
        PrintList(alist_Artist)

    # Sort CDS by Genre
    if Option == 4:
        alist_Genre = SortByGenre(aList)
        PrintList(alist_Genre)

    # Sort CDs by Price
    if Option == 5:
        alist_Price = SortByPrice(aList)
        PrintList(alist_Price)

    # Find All CDs by Title
    if Option == 6:
        Title = input('Enter the title:')
        Find_title = FindByTitle(Title, aList)
        if Find_title == []:
            print('Unfortunately, The title you input is not in this CD list ')
        else:
            PrintList(Find_title)

    # Find All CDs by Artist
    if Option == 7:
        Artist = input('Enter the artist:')
        Find_Artist = FindByArtist(Artist, aList)
        if Find_Artist == []:
            print('Unfortunately, The artist you input is not in this CD list')
        else:
            PrintList(Find_Artist)

    # Find All CDs by Genre
    if Option == 8:
        Genre = input('Enter the genre:')
        Find_Genre = FindByGenre(aList, Genre)
        if Find_Genre == []:
            print('Unfortunately, Your favourite genre is not in this CD list')
        else:
            PrintList(Find_Genre)

    # Find All CDs with Price at Most Price X
    if Option == 9:
        Price = float(input('Target Price:'))
        Find_Most_Price = FindByPrice(aList, Price)
        if Find_Most_Price == []:
            print('Unfortunately, Your target price is lower than cheapest price')
        else:
            PrintList(Find_Most_Price)

    # Quit
    if Option == 10:
        return


result = decision(Option, aList)

## Close the file
file_r.close()




