
import re
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

list = get_file_data("input.txt")
# build a 2D List based on the file_data
map = []
for line in list:
    row = []
    for letter in line:
        row.append(letter)
    map.append(row)

# notes on maybe how to solve this
# search through the map until an antenna is found. store its frequency. for every antenna found,
# for every antenna found with the same frequency,
# store its position RELATIVE to the first antenna with that frequency.
# DOUBLE the list of positions and modify the map to include the antidotes there
# REVERSE the list of positions and modify the map to include them
# before changing, check if that position is empty.
# add the antenna's frequency to a "dont search this" list and repeat for every unique antenna.

dontSearch = []
def checkBounds(x,y): #given x and y, check if x >= 0 and <= len(map[0])-1
    if 0 <= x <= len(map[0])-1 and 0 <= y <= len(map) - 1:
        print("inBounds")
        return True
    print(str(x) + ", " + str(y) + ":  " + "outOfBounds")
    return False

def placeXforOneAntenna(ox,oy): #given ONE antenna location, find the other antenna and double/reverse relative positions to include the Xs
    freq = map[oy][ox] # x is horizontal y is vertical
    listOfRelPos = []
    print(freq)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == freq and (not (y == oy and x == ox)):
                listOfRelPos.append("(" + str(x-ox) + ", " + str(y-oy) + ")")
    print(listOfRelPos) # position relative the first antenna. elements are in deltaY, deltaX
    for i in range(len(listOfRelPos)):
        firstSearch = "\\(-?[0-9]{1,2}"
        secondSearch = "-?[0-9]{1,2}\\)"
        ldeltaY=re.findall(firstSearch, listOfRelPos[i])
        ldeltaX=re.findall(secondSearch, listOfRelPos[i])
        deltaX = ldeltaX[0]
        deltaY = ldeltaY[0]

        deltaX = deltaX[:-1]
        deltaY = deltaY[1:]
        print(deltaX)
        print(deltaY)
        if checkBounds(ox+int(deltaX)*2,oy+int(deltaY)*2) and map[oy+int(deltaY)*2][ox+int(deltaX)*2] == '.':
            print("placed X!")
            map[oy+int(deltaY)*2][ox+int(deltaX)*2] = "X"
        if checkBounds(ox + int(deltaX) * -1, oy + int(deltaY) * -1) and map[oy + int(deltaY) * -1][ox + int(deltaX) * -1] == '.':
            print("placed X!")
            map[oy + int(deltaY) * -1][ox + int(deltaX) * -1] = "X"
    print(listOfRelPos)

for i in map:
    print(i)

placeXforOneAntenna(7,5)

for i in map:
    print(i)
