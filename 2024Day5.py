
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



def checkUpdateOrderThenAddMiddleNumber():
    sumOfMiddleNums = 0
    # rules - for each update, look for the first number. take its index.
    # then look for the second number. take its index. if index 2 < index 1, invalid.
    for u in range(len(updates)):
        for r in range(len(rules)):
            firstNumIndex = -1
            secondNumIndex = -1
            # each number is always 2 digits long
            firstNum = rules[r][0:1]
            secondNum = rules[r][3:4]
            for num in range(len(updates[u])):
                if firstNum in updates[u]: #if found, look through updates[u] to see where
                    firstNumIndex = u
                if secondNum in updates[u]:
                    secondNumIndex = u
            if not (firstNumIndex == -1) and not (secondNumIndex == -1):
                if int(firstNumIndex) < int(secondNumIndex): #this makes it valid!
                    sumOfMiddleNums += int(updates[u][len(updates[u])//2])
                    print("weewoo" + str(int(updates[u][len(updates[u])//2])))
    return sumOfMiddleNums

print(checkUpdateOrderThenAddMiddleNumber())
