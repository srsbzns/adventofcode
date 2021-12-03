# NO LIBRARIES
# STDLIB ONLY
# FINAL DESTINATION

def format_commands(commands):
    program = [i.rstrip().split() for i in commands]
    return program

def execute_program(program):
    horizontal_pos = 0
    depth = 0
    for i in program:
        match i:
            case ['forward',n]:
                horizontal_pos += int(n)
            case ['down',n]:
                depth += int(n)
            case ['up',n]:
                depth -= int(n)
    return horizontal_pos * depth

def main():
    with open('input.txt', 'r') as f:
        input = f.readlines()
    program = format_commands(input)
    print(execute_program(program))

main()