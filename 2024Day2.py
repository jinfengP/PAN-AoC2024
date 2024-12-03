def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data
list = get_file_data("input.txt")
levels = []
for i in range(len(list)):
    levels.append(list[i].split(" ")) # 2d array


def horriblySolvedPartOnePart(lastNumber):
    safeCount = 0
    for i in range(len(levels)):
        for j in range(len(levels[i])-1):#check if two are same
            safe = True
            diff = int(levels[i][j+1]) - int(levels[i][j]) # if diff >0, increasing. if <0, decreasing
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False
            else:
                safe=False
                break
            if abs(diff) > 3: # if difference is 4 or more, its unsafe.
                safe = False
                break
            levels[i].append(lastNumber) # phase two: check if it changes direction
            j+=1
            diff = int(levels[i][j+1]) - int(levels[i][j])
            levels[i].pop()
            if increasing and diff < 0:
                safe = False
                break
            if not increasing and diff > 0:
                safe = False
                break
        if safe:
            safeCount+=1    
    return safeCount


def partOne():
    sum = int(horriblySolvedPartOnePart(9999999))
    sum += int(horriblySolvedPartOnePart(-9999999))
    return sum

print(partOne())