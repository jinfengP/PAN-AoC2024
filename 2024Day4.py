
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("input.txt")
# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)
# grid is our really large 2d array

def xmasCrossword():
    booleanList = ['canSearchHorizontallyLeft','canSearchHorizontallyRight','canSearchVerticallyUp','canSearchVerticallyDown',
        'canSearchDiagonallyUpLeft','canSearchDiagonallyUpRight','canSearchDiagonallyDownLeft','canSearchDiagonallyDownRight']
    countxmas = 0
    for r in range(len(grid)):
        for e in range(len(grid[r])):
            for i in range(len(booleanList)):
                booleanList[i] = True
            if grid[r][e] == "X":
                canSearchList = [] # after locating x, cansearchlist includes only the directions that "MAS" can go in.
                if r < 3: # TOP EDGE
                    booleanList[2] = False
                    booleanList[4] = False
                    booleanList[5] = False
                if r > len(grid) - 4: # BOTTOM EDGE
                    booleanList[3] = False
                    booleanList[6] = False
                    booleanList[7] = False
                if e < 3: # LEFT EDGE
                    booleanList[0] = False
                    booleanList[4] = False
                    booleanList[6] = False
                if e > len(grid[r]) - 4: # RIGHT EDGE
                    booleanList[1] = False
                    booleanList[5] = False
                    booleanList[7] = False
                for searchOption in booleanList:
                    if searchOption:
                        canSearchList.append(searchOption)
                if booleanList[0]:
                    if grid[r][e-1] == "M" and grid[r][e-2] == "A" and grid[r][e-3] == "S":
                        countxmas+=1
                if booleanList[1]:
                    if grid[r][e+1] == "M" and grid[r][e+2] == "A" and grid[r][e+3] == "S":
                        countxmas+=1
                if booleanList[2]:
                    if grid[r-1][e] == "M" and grid[r-2][e] == "A" and grid[r-3][e] == "S":
                        countxmas+=1
                if booleanList[3]:
                    if grid[r+1][e] == "M" and grid[r+2][e] == "A" and grid[r+3][e] == "S":
                        countxmas+=1
                if booleanList[4]:
                    if grid[r-1][e-1] == "M" and grid[r-2][e-2] == "A" and grid[r-3][e-3] == "S":
                        countxmas+=1
                if booleanList[5]:
                    if grid[r-1][e+1] == "M" and grid[r-2][e+2] == "A" and grid[r-3][e+3] == "S":
                        countxmas+=1
                if booleanList[6]:
                    if grid[r+1][e-1] == "M" and grid[r+2][e-2] == "A" and grid[r+3][e-3] == "S":
                        countxmas+=1
                if booleanList[7]:
                    if grid[r+1][e+1] == "M" and grid[r+2][e+2] == "A" and grid[r+3][e+3] == "S":
                        countxmas+=1
    return countxmas

def crossmasFinder():
    for r in range(len(grid)):
        for e in range(len(grid[r])):
            if grid[r][e] == "A":
                if e < 1 or e > len(grid[r]) - 2 or r > len(grid) - 2 or r < 1: # IF NOT TOUCHING THE EDGES
                    
                    
