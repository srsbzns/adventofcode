def change_directory(line):
    command = line.split()
    new_directory = command[2]
    return new_directory

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

    for line in input:
        if line[0] == "$":
            if line[2:3] == "cd":
                current_directory = change_directory(line)
            elif line[]
                pass


