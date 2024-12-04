
import re
def get_file_data(file_name):
    f = open(file_name)
    data = ""
    for line in f:
        data += (line.rstrip())
    return data # a string of LITERALLY EVERYTHING.

searchString = get_file_data("input.txt")

def filterAndMultiply():
    sumOfProducts = 0
    numList = []
    regex = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"
    filteredData = re.findall(regex,searchString)
    for i in range(len(filteredData)):
        firstNumSearch = "[0-9]{1,3}"
        numList.append(re.findall(firstNumSearch,filteredData[i]))
    for index in range(len(numList)):
        sumOfProducts += int(numList[index][0]) * int(numList[index][1])
    #     print("Current Sum: " + str(sumOfProducts) + " by adding the product of " + str(numList[index][0]) + " and " + str(numList[index][1]))
    # print("Sum: " + str(sumOfProducts))
    # print("Filtered Data: " + str(filteredData))
    return sumOfProducts

def partTwo():
    sumOfProducts = 0
    consider = True
    numList = []
    regex = "mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)"
    filteredData = re.findall(regex,searchString) # GOOD
    for i in range(len(filteredData)):
        firstNumSearch = "[0-9]{1,3}"
        numList.append(re.findall(firstNumSearch,filteredData[i])) #includes length 0 arrays which are either do() or don't()
    for i in range(len(numList)):
        if filteredData[i] == "do()":
            consider = True
        elif filteredData[i] == "don't()":
            consider = False
        else:
            if consider:
                sumOfProducts += int(numList[i][0]) * int(numList[i][1])
    return sumOfProducts


