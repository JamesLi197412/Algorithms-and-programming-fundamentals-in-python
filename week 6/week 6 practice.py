
def task1():
    # Task 1 Coin reduce
    Denominations = input('Please enter denominations : ')
    Amount = int(input('Please enter the amount you want to change: '))
    Denominations = Denominations.split(',')

    for i in range(len(Denominations)):
        Denominations[i] = int(Denominations[i])

    def greedyCoinDenom(Denominations, Amount):
        coinused = [0] * len(Denominations)
        trialCoin = len(Denominations) - 1
        while Amount > 0 and trialCoin > 0:
            use = 0
            if Denominations[trialCoin] <= Amount:
                use = Amount // Denominations[trialCoin]
                Amount = Amount - use * Denominations[trialCoin]
                coinused[trialCoin] = use
            trialCoin = trialCoin - 1

        if Amount > 0:
            print('Impossible')
            return None

        return coinused

    def display_coin_used(coinused, Denominations):
        for index in range(len(Denominations)):
            if coinused[index] > 0:
                print(coinused[index], '*', Denominations[index], end=' ')

    coinused = greedyCoinDenom(Denominations, Amount)

    display_coin_used(coinused, Denominations)

def task2():
    ## Task 2: Knapsack Problem
    filename = input('Please enter file name with item details: ')
    fileopen = open(filename)  # Or f=open('items.txt')

    read = []
    values = []
    weights = []
    for line in fileopen:
        read.append(line)

    for index in range(len(read)):
        read[index] = read[index].split()
        theValue = read[index][1][1:]
        theWeight = read[index][0][:-2]
        values.append(int(theValue))
        weights.append(int(theWeight))

    def extendable(weights, used, current, maxWeight):
        for position in range(len(weights)):
            if current + weights[position] <= maxWeight and (used[position] < 0):
                return True
        return False

    def markNotUsed(weights, used, current, maxWeight):
        for position in range(len(weights)):
            if used[position] < 0:
                if current + weights[position] > maxWeight:
                    used[position] = 0

    def maxRatio(ratios, used):
        maxPos = None  # Default value
        for index in range(len(used)):
            if used[index] == -1:  # not yet used or excluded
                if maxPos is None:
                    maxPos = index
                elif ratios[maxPos] < ratios[index]:
                    maxPos = index

        return maxPos

    def greedyMaxRatio(values, weights, maxWeight):
        bitList = [-1] * len(values)
        ratios = [0] * len(values)
        total_cost = 0
        total_weight = 0
        for index in range(len(values)):
            ratios[index] = values[index] / weights[index]

        while extendable(weights, bitList, total_weight, maxWeight):
            markNotUsed(ratios, bitList, total_weight, maxWeight)
            best = maxRatio(ratios, bitList)
            bitList[best] = 1
            total_cost += values[best]
            total_weight += weights[best]

        return bitList

    print(greedyMaxRatio(values, weights, 7))

    fileopen.close()

def task3():
    ##Task 3 Calorie problem
    cups = int(input('Please enter the number of cupcakes: '))

    def costOfCake(cups, calory):
        return (2 ** cups) * calory

    def orderedCost(cups, calory_list):
        totalCost = 0
        for index in range(len(calory_list)):
            totalCost += costOfCake(calory_list[index], cups[index])

        return totalCost

    def getMinUnused(calory_list, used):
        minPos = None
        for index in range(len(used)):
            if used[index] == None:  # not yet used
                if minPos is None:
                    minPos = index
                elif calory_list[minPos] < calory_list[index]:
                    minPos = index

        return minPos

    def cupcakeGreed(calory_list):
        used = [None] * len(calory_list)  # represents which we have used so far
        lastUsed = 0
        while lastUsed < len(calory_list):
            position = getMinUnused(calory_list, used)

            used[position] = lastUsed
            lastUsed += 1

        cost_of_cakes = orderedCost(calory_list, used)

        return cost_of_cakes, used

    cost, orderUsedIn = cupcakeGreed([1, 3, 2])
    print('Marc shold run', str(cost) + '_miles')

