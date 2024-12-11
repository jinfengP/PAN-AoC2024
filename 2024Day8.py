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
for i in map:
    print(i)

dontSearch = []
def checkBounds(x,y): #given x and y, check if x >= 0 and <= len(map[0])-1
    if 0 <= x <= len(map[0])-1 and 0 <= y <= len(map) - 1:
        return True
    print("outOfBounds")
    return False

def placeXforOneAntenna(oy,ox): #given ONE antenna location, find the other antenna and double/reverse relative positions to include the Xs
    freq = map[ox][oy] # x is horizontal y is vertical
    listOfRelPos = []
    print(freq)
    for x in range(len(map)):
        for y in range(len(map)):
            if map[x][y] == freq:
                listOfRelPos.append("(" + str(x-ox) + ", " + str(y-oy) + ")")
    print(listOfRelPos) # position relative the first antenna. elements are in deltaY, deltaX
    for i in range(len(listOfRelPos)):
        r = listOfRelPos[i].replace("(",'')
        r = r.replace(")",'')
        listOfRelPos[i] = r.replace(', ','')
    print(listOfRelPos)



placeXforOneAntenna(8,1)
