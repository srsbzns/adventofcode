# detect start-of-packet marker in datastream (a sequence of X characters that are all different)

with open('input.txt', 'r') as file:
        input = file.read()

# set the length of the start-of-packet marker window
sop_marker_length = 14

i = 0
while i < len(input):
    capture_window = set(input[i:i+sop_marker_length])
    if len(capture_window) == sop_marker_length:
        print(i+sop_marker_length)
        break
    else:
        i += 1
