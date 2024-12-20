
def get_rules(file_name):
    f = open(file_name)
    data = []
    for line in f:
        if "|" in line:
            data.append(line.rstrip())
    return data

def get_updates(file_name):
    f = open(file_name)
    data = []
    for line in f:
        if not "|" in line:
            data.append(line.rstrip().split(",")) # 2d array
    data.pop(0) # removes the first item, which is a [] because theres an empty line in the input file
    return data
rules = get_rules("input.txt")
updates = get_updates("input.txt")
badUpdates = [["000"]]


def checkUpdateOrderThenAddMiddleNumber():
    sumOfMiddleNums = 0
    # for each update, look for the first number. take its index.
    # then look for the second number. take its index. if index 2 < index 1, invalid.
    for u in range(len(updates)):
        ruleBroken = False
        sumOfCurrentRow = 0
        for r in range(len(rules)):
            firstNumIndex = -1
            secondNumIndex = -1
            # each number is always 2 digits long
            firstNum = rules[r][0:2]
            secondNum = rules[r][3:5]
            for num in range(len(updates[u])):
                if firstNum in updates[u][num]: #if found, look through updates[u] to see where
                    firstNumIndex = num
                if secondNum in updates[u][num]:
                    secondNumIndex = num
            if not (firstNumIndex == -1) and not (secondNumIndex == -1): #if both are found then
                if (not ruleBroken) and (int(firstNumIndex) < int(secondNumIndex)): #this makes it valid!
                    sumOfCurrentRow = int(updates[u][len(updates[u])//2])
                elif (int(firstNumIndex) > int(secondNumIndex)):
                    ruleBroken = True
                    if not badUpdates[-1] == updates[u]: # to prevent multiple rulebreaks in a row to be added to badUpdates
                        badUpdates.append(updates[u])
                    sumOfCurrentRow = 0
        sumOfMiddleNums += sumOfCurrentRow
    return sumOfMiddleNums

def fixUnorderedUpdatesAndAccumulate(): # yeah i have no idea how
    checkUpdateOrderThenAddMiddleNumber()
    badUpdates.pop(0)
    print(badUpdates + " <-- Before Change")
    for u in range(len(badUpdates)):
        for r in range(len(rules)):
            firstNum = rules[r][0:2]
            secondNum = rules[r][3:5]
            for num in range(len(badUpdates[u])):
                if firstNum in badUpdates[u][num]: #if found, look through updates[u] to see where
                    firstNumIndex = num
                if secondNum in badUpdates[u][num]:
                    secondNumIndex = num
        badUpdates[u][secondNumIndex] = firstNum
        badUpdates[u][firstNumIndex] = secondNum
    print(badUpdates + " <-- After Change")

fixUnorderedUpdatesAndAccumulate()
                
