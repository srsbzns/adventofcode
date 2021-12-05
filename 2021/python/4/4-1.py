# get raw inputs from puzzle input file
def ingest_inputs(input_file):
    with open(input_file, 'r') as f:
        draws_input = f.readline()
        boards_input = f.read()
        inputs = {'draws':draws_input,'boards':boards_input}
    
    return inputs

# create draws[] from input
def create_draws(draws_input):
    #format the input
    draws_output = draws_input.strip().split(sep=',')
    draws_output = [int(i) for i in draws_output]

    return draws_output

# create boards[] from input
def create_boards(boards_input):
    # remove newlines
    formatted_boards_input = boards_input.split(sep='\n')
    
    # split the input into individual boards
    boards_output = []
    board_number = -1
    for row in formatted_boards_input:
        match row:
            # empty line indicates break between boards, so make new board
            case str(row_string) if row_string == '':
                board_number += 1
                boards_output.append([])
            # if line not empty, it's part of the board
            case str(row_string) if row_string != '':
                boards_output[board_number].append(row_string.split())

    # replace board values with dictionary objects
    for z, board in enumerate(boards_output):
        for x, row in enumerate(board):
            for y, number in enumerate(row):
                boards_output[z][x][y] = {'number':int(number),'marked':False}

    return boards_output

# analyze a board for bingo
def check_bingo(board,row,col):
    # check for bingo across row
    row_list = [board[row][i]['marked'] for i, x in enumerate(board)]
    match row_list:
        case [*row_vals] if sum(row_vals) == len(row_list):
            return True
    # check for bingo across col
    col_list = [board[i][col]['marked'] for i, x in enumerate(board)]
    match col_list:
        case [*col_vals] if sum(col_vals) == len(col_list):
            return True

def calculate_score(win_board, win_num):
        unmarked_numbers = 0
        for x, row in enumerate(win_board):
            for y, col in enumerate(row):
                match col:
                    case {'number':int(n),'marked':False}:
                        unmarked_numbers += n
        return unmarked_numbers * win_num

# meat and potatos, this is where we "play" the game
def play_bingo(draws, boards):
    numbers_called = 0
    for i, number in enumerate(draws):
        numbers_called += 1
        for z, board in enumerate(boards):
            for x, row in enumerate(board):
                for y, col in enumerate(row):
                    match col:
                        case {'number':int(n),'marked':False} if n == number and numbers_called < 5:
                            col['marked'] = True
                        case {'number':int(n),'marked':False} if n == number and numbers_called >= 5:
                            col['marked'] = True
                            if check_bingo(board,x,y) == True:
                                return calculate_score(board, number)
 

def main(input):
    # open puzzle input file and generate inputs
    raw_inputs = ingest_inputs(input)
    # create draws list
    draws = create_draws(raw_inputs['draws'])
    # create boards list
    boards = create_boards(raw_inputs['boards'])
    print(play_bingo(draws, boards))

main('input.txt')