# crates are not uniquely marked, and are marked with single uppercase letter (some repeating)
# there are 9 "stacks" (columns) of up to 8 (rows) of crates
# lines 1-8 are crate locations in the array
# line 9 is the array column header
# line 10 is a newline
# the rest of the lines are instructions declaring a number of move operations (move 1), the column indicator 
# to execute from (from 7) and the column indicator to execute to (to 2) (MOVE CRATE FROM 7 TO 2 1 TIME)

# Given a 2D array and a column to search, return the highest row position occupied by a crate
def top_crate_finder(array,column):
    row = 0
    while row < len(array):
        if array[row][column] == ' ':
            row += 1
        else:
            break
    
    # if the row variable reaches a number bigger than the number of rows, that 
    # SHOULD mean the column in question is totally empty.
    return row

raw_docks_array, raw_moves_list = [], []

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

    # split input between docks_array and raw_moves_list, ignoring the "column indicator" row
    for count, line in enumerate(input):
        if line == '' or line[1] == "1":
            pass
        elif line[0] != "m":
            raw_docks_array.append(line)
        else:
            raw_moves_list.append(line)

#format the docks array
#start at row[1] (the first location of an actual crate marking) and increment by 4 
docks_array = []
for count, row in enumerate(raw_docks_array):
    formatted_row = []
    for location in range(1, len(row), 4):
        formatted_row += [row[location]]
    docks_array.append(formatted_row)

# find maximum size array could be based on number of columns times number of rows
# and expand the array to that size
max_array_size = len(docks_array[0]) * len(docks_array)
while len(docks_array) < max_array_size:
    docks_array = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]] + docks_array

# The above results in docks_array[rows][columns], with rows in top-down order 

# format the moves list
moves_list = []
for string in raw_moves_list:
    elements = string.split(' ')
    moves_list.append((elements[1:6:2]))

for i in range(len(moves_list)):
    moves_list[i] = [int(i) for i in moves_list[i]]


# this whole thing should probably be a function
for repetitions,origin_column,destination_column in moves_list:
    origin_column -= 1
    destination_column -=1
    # loop for the number of moves?
    for i in range(repetitions):
        # find the current crate on "top" of the origin column;
        # need to cut "down" the x axis across the y axes (docks_array[0:8][move[1]])

        # to do this, we're going to first the marking of the crate currently on top of the origin column
        target_crate_origin = top_crate_finder(docks_array,origin_column)
        target_crate_mark = docks_array[target_crate_origin][origin_column]

        # now we need to find the crate on top of the destination column, so we can put 
        # the target crate on top of it
        target_crate_destination = top_crate_finder(docks_array,destination_column)-1
        docks_array[target_crate_destination][destination_column] = target_crate_mark

        # now we go back and mark the origin crate location as empty
        docks_array[target_crate_origin][origin_column] = ' '

# finally, we get the mark of every column's top crate and sum for our "message"
top_crates_message = ''
for i in range(len(docks_array[0])):
    top_crate_mark = docks_array[top_crate_finder(docks_array,i)][i]
    top_crates_message += top_crate_mark

print(top_crates_message)
