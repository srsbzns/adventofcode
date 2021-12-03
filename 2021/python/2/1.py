# NO LIBRARIES
# STDLIB ONLY
# FINAL DESTINATION

with open('input.txt', 'r') as f:
    input = f.readlines()

commands = [i.rstrip().split() for i in input]

horizontal_pos = 0
depth = 0

for i in commands:
    if i[0] == 'forward':
        horizontal_pos += int(i[1])
    elif i[0] == 'down':
        depth += int(i[1])
    elif i[0] == 'up':
        depth -= int(i[1])

print(horizontal_pos * depth)