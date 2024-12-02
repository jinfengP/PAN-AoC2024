def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


list = get_file_data("2024Day1.txt")
# you now have a list of Strings from the input file
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
sum = 0

for i in range(len(list)):
    num1 = list1[i]
    count = 0
    for j in range(len(list)):
        if num1 == list2[j]:
            count+=1
    sum += int(num1) * count
print(sum)