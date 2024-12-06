
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
# build a 2D List based on the file_data
map = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    map.append(row)
# map is our really large 2d array

movingUp = True
movingRight = False
movingDown = False
movingLeft = False

def findGuard(choice):
    for r in range(len(map)):
        for c in range(len(map[r])):
            if not (map[r][c] == "." or map[r][c] == "X" or map[r][c] == "#"):
                if choice == "xpos":
                    return c
                elif choice == "ypos":
                    return r
                else:
                    return 0000

def checkObstruction():
    x = findGuard("xpos")
    y = findGuard("ypos")
    if movingUp:
        if map[x][y-1] == "#":
            return True
    elif movingLeft:
        if map[x-1][y] == "#":
            return True
    elif movingRight:
        if map[x+1][y] == "#":
            return True
    elif movingDown:
        if map[x][y+1] == "#":
            return True
    return False
# ^ returns true if there is an obstacle in the way


def calculateGuardMoves(): # whilst the guard is NOT on the edge of the map,
    while not (findGuard("xpos") > 0) or (findGuard("xpos") < len(map[0])-1) or (findGuard("ypos") > 0) or (findGuard("ypos") < len(map)-1):
        if not checkObstruction():
            x = findGuard("xpos")
            y = findGuard("ypos")
            map[x][y] = "X"
            if movingUp:
                map[x][y-1] = "^"
            elif movingRight:
                map[x+1][y] = "^"
            elif movingDown:
                map[x][y+1] = "^"
            elif movingLeft:
                map[x-1][y] = "^"
        elif checkObstruction():
            if movingUp:
                movingUp = False
                movingRight = True
            elif movingRight:
                movingRight = False
                movingDown = True
            elif movingDown:
                movingDown = False
                movingLeft = True
            elif movingLeft:
                movingLeft = False
                movingUp = True
calculateGuardMoves()
print(map)

