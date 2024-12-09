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

def findGuard(choice):
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == "^": # map(y,x) why does it do this
                if choice == "xpos":
                    return r
                elif choice == "ypos":
                    return c

def checkObstruction():
    x = findGuard("xpos")
    y = findGuard("ypos")
    if ((y > 0) and (y < len(map[0])-1) and (x > 0) and (x < len(map)-1)):
        if movingUp:
            if map[x-1][y] == "#":
                return True
        elif movingLeft:
            if map[x][y-1] == "#":
                return True
        elif movingRight:
            if map[x][y+1] == "#":
                return True
        elif movingDown:
            if map[x+1][y] == "#":
                return True
        return False
    return False
# ^ returns true if there is an obstacle in the way


def calculateGuardMovesAndCountX(): # whilst the guard is NOT on the edge of the map,
    global movingUp
    global movingRight
    global movingDown
    global movingLeft
    while ((findGuard("ypos") > 0) and (findGuard("ypos") < len(map[0])-1) and (findGuard("xpos") > 0) and (findGuard("xpos") < len(map)-1)):
        if not checkObstruction():
            x = findGuard("xpos")
            y = findGuard("ypos")
            map[x][y] = "X"
            if movingUp:
                map[x-1][y] = "^"
            elif movingRight:
                map[x][y+1] = "^"
            elif movingDown:
                map[x+1][y] = "^"
            elif movingLeft:
                map[x][y-1] = "^"
        else:
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
    count = 1
    for r in range(len(map)):
        for c in range(len(map)):
            if map[r][c] == "X":
                count+=1
    return count


movingUp = True
movingRight = False
movingDown = False
movingLeft = False

print(calculateGuardMovesAndCountX())

