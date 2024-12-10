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
# search through the map until an antenna is found. store its frequency. for every antenna with the same frequency,
# store its position RELATIVE to the first antenna with that frequency.
# DOUBLE the list of positions and modify the map to include the antidotes
# before changing, check if that position is empty.
# add the antenna's frequency to a "dont search this" list and repeat for every unique antenna.