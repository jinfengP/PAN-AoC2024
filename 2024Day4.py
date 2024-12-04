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
booleanList = ['canSearchHorizontallyLeft','canSearchHorizontallyRight','canSearchVerticallyUp','canSearchVerticallyDown',
    'canSearchDiagonallyUpLeft','canSearchDiagonallyUpRight','canSearchDiagonallyDownLeft','canSearchDiagonallyDownRight']
countxmas = 0
for r in range(len(grid)):
    for e in range(len(grid[r])):
        for i in range(len(booleanList)):
            booleanList[i] = True;
        if grid[r][e] == "X":
            canSearchList = []
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
            
