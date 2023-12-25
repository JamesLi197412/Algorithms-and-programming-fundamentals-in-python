def task1():
    ##  Some information on heaps:

    heapList = [8, 4, 7, 2, 3, 1]
    integer = 0

    def findChildren(heapList, integer):
        if integer <= 0:
            return False
        elif integer >= len(heapList):
            return False
        elif integer * 2 >= len(heapList):
            return False
        elif integer * 2 == len(heapList) - 1:
            print('Parent: ', str(heapList[integer]))
            print('Left Child: ', str(heapList[integer * 2]))
            return True
        else:
            print('Parent: ', str(heapList[integer]))
            print('Left Child: ', str(heapList[integer * 2]))
            print('Right Child: ', str(heapList[integer * 2 + 1]))

            return True

    for position in range(0, len(heapList)):
        findChildren(heapList, position)


def task2():
    ## Task 2 Investigate time taken by two different algorithms for computing x**n
    import random
    import timeit

    def power1(x, n):
        #   Computes x to the power of n
        value = 1
        for k in range(n):
            value *= x

        return value

    def power2(x, n):
        #   computes x to the power of n
        value = 1
        if n > 1:
            value = power2(x, n / 2)
        if n % 2 == 0:
            value = value * value
        else:
            value = value * value * x

        return value

    count1 = 0
    count2 = 0
    for i in range(100):
        #   Genertae random integers for x and n
        x = random.randrange(1, 100)
        n = random.randrange(1, 100)

        #   Start timing power1
        start = timeit.default_timer()
        power1(x, n)

        #   Finish timing power1
        end = timeit.default_timer()

        print(' Time taken by power1 was: {} seconds.'.format(end - start))

        #   Start timing power2
        start = timeit.default_timer()
        power2(x, n)

        #   Finish timing power2
        end = timeit.default_timer()

        print(' Time taken by power 2 was {} seconds.'.format(end - start))


def task3():
    ##  Task 3

    def quicksort(myList, start, end):
        if start < end:
            #   partition the list
            pivot = partition(myList, start, end)

            #   sort both halves
            quicksort(myList, start, pivot - 1)
            quicksort(myList, pivot + 1, end)

        return myList

    def partition(myList, start, end):
        pivot = myList[start]
        left = start + 1
        right = end
        done = False
        while not done:
            while left <= right and myList[left] <= pivot:
                left = left + 1
            while myList[right] >= pivot and right >= left:
                right = right - 1

            if right < left:
                done = True
            else:
                #   swap places
                temp = myList[left]
                myList[left] = myList[right]
                myList[right] = temp

        #   swap start with myList[right]
        temp = myList[start]
        myList[start] = myList[right]
        myList[right] = temp

        return right

    def selectionSort(array):
        vendor = len(array)
        for position in range(vendor - 1):
            minRow = position
            for temp in range(position + 1, vendor):
                if array[temp] < array[minRow]:
                    minRow = temp
                array[position], array[minRow] = array[minRow], array[position]

    def timesort(List):
        #   print(List)
        List1 = List[:]
        List2 = List[:]
        sStart = timeit.default_timer()
        selectionSort(List1)
        sTime = timeit.default_timer() - sStart

        #   Finish timint

    import random
    import timeit
    sBest = float('inf')
