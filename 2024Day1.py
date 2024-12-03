def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data
list = get_file_data("input.txt")

list1 = [] #first half of pair
list2 = [] #the other pair
for i in range(len(list)):
    num1 = list[i].split("   ")[0]
    num2 = list[i].split("   ")[1]
    list1.append(num1)
    list2.append(num2)
# splits it into two lists each with half the pair
list1.sort()
list2.sort()

def totalDistance(): # PART ONE---------------------
    sum = 0
    for i in range(len(list)):
        diff = int(list1[i]) - int(list2[i])
        sum += abs(diff)
    return sum


def calculateSimilarity(): # PART TWO---------------
    sum = 0
    for i in range(len(list)):
        num1 = list1[i]
        count = 0
        for j in range(len(list)):
            if num1 == list2[j]:
                count+=1
        sum += int(num1) * count
    return sum

print(totalDistance())
print(calculateSimilarity())
