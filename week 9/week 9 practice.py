def task1():
    # Task 1: Use recursive

    def binarySearch2(L, target, start, end):
        mid = (start + end) // 2
        if start == end:
            return False
        if L[mid] == target:
            return mid
        elif L[mid] > target:
            return binarySearch2(L, target, start, mid - 1)
        elif L[mid] < target:
            return binarySearch2(L, target, mid + 1, end)


def task2():
    # Task 2 : Fractorial values by recursive function
    import math

    def fractional(n):
        if n == 1:
            L = [0] * n
            L[0] = 1

        else:
            L = fractional(n - 1)
            L.append(n * L[n - 2])

        return L

    n = int(input('Enter the input: '))

    print(fractional(n))

def task3():
    # Task 3: printStars

    def fractional(n):
        if n == 1:
            L = [0] * n
            L[0] = 1

        else:
            L = fractional(n - 1)
            L.append(n * L[n - 2])

        return L

    n = int(input('Enter the input: '))

    L = fractional(n)

    def printStars(n):
        for i in n:
            print('*' * i)

    printStars(L)

    print(L)

def task4():
    ## Task 4 Interesting Brackets

    Brackets = input('Enter string of brackets: ')

    def indexIn(target, list):
        spot = 0
        while spot < len(list):
            if list[spot] == target:
                return spot
        return -1

    def bracketsMatch(anExpression):
        opening = ['[', '{', '(']
        closing = [']', '}', ')']

        stack = []

        for char in anExpression:
            openFind = indexIn(char, opening)
            closeFind = indexIn(char, closing)
            if openFind >= 0:
                stack.append(char)
            elif closeFind >= 0:
                current = stack.pop()  # Remove the item at the given position in the list, and return it.
                # If no index is specified, a.pop() removes and returns the last item in the list.

                if current == opening[closeFind]:
                    pass  ##Great move on
                else:
                    return False  # Mismatch

            else:
                pass  # Not a bracket,ignore this character

        if len(stack) == 0:  # no mismatched left
            return True
        else:
            return False

    print(bracketsMatch(Brackets))


def task5():
    ## Task 5 Order Service for a resturant
    queue = []
    count = 0

    while len(queue) > 0 and count > 0:  # Just so we do it at least once and until it's done
        serve = input('Is any order served ? ')

        if serve.lower == ' no ':
            orderNum = input('Please enter order Number')
            queue.append(orderNum)
        else:
            queue.pop(0)  # then serve

        print(' The order list is :'
        queue)
