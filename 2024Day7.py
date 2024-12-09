def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


list = get_file_data("input.txt")


def findCombinationOfMultAndAdd(testValue, factors):
    listOfAllCombinations = []
    for i in range(len(factors)-1):
        if not len(listOfAllCombinations) == 0:
                for j in range(len(listOfAllCombinations)):
                    multByNext = int(listOfAllCombinations[j]) * int(factors[i+1])
                    addByNext = int(listOfAllCombinations[j]) + int(factors[i+1])
                    listOfAllCombinations.append(multByNext)
                    listOfAllCombinations.append(addByNext)
        else:
            multByNext = int(factors[i]) * int(factors[i+1])
            addByNext = int(factors[i]) + int(factors[i+1])
            listOfAllCombinations.append(multByNext)
            listOfAllCombinations.append(addByNext)
    for i in listOfAllCombinations:
        if int(testValue) == int(i):
            return True
    return False

sumOfTestValues = 0

for index in range(len(list)):
    testValue = list[index].split(":")[0]  # the number before the semicolon. is correct
    factors = list[index].split(":")[1].split(" ")
    factors.pop(0)  # list of the numbers after the semicolon. is correct
    if (findCombinationOfMultAndAdd(testValue, factors)):
        sumOfTestValues += int(testValue)

print(str(sumOfTestValues))