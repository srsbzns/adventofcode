def format_commands(commands):
    program = [i.rstrip().split() for i in commands]
    return program

def execute_program(program):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in program:
        match i:
            case ['forward',n]:
                horizontal_pos += int(n)
                depth += aim * int(n)
            case ['down',n]:
                aim += int(n)
            case ['up',n]:
                aim -= int(n)
    return horizontal_pos * depth

def main():
    with open('input.txt', 'r') as f:
        input = f.readlines()
    program = format_commands(input)
    print(execute_program(program))

main()