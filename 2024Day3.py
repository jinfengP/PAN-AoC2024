
import re
def get_file_data(file_name):
    f = open(file_name)
    data = ""
    for line in f:
        data += (line.rstrip())
    return data # a string of LITERALLY EVERYTHING.


searchString = get_file_data("input.txt")


def partOne():
    sumOfProducts = 0
    firstNumList = []
    secondNumList = []
    regex = "mul\\([1-9]{1,3},[1-9]{1,3}\\)"
    filteredData = re.findall(regex,searchString)
    print(filteredData)
    for element in filteredData:
        print(element)
        firstNumSearch = "\\([1-9]{1,3}"
        firstNumList = re.findall(firstNumSearch,element)
        print(firstNumList)
    return sumOfProducts
partOne()