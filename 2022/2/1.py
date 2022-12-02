# Rock Paper Scissors
# 2 players (player 1 + player 2)

# col 1 = opponent throw
# col 2 = my throw

# Point Breakdown
# 1 for Rock
# 2 for Paper
# 3 for Scissors

# 0 if you lost
# 3 if the round was a draw
# 6 if you won

# Open the input as a file object

rock = 1
paper = 2
scissors = 3

loss = 0
draw = 3
win = 6

total_score = 0

# update to Python 3.10+ and redo with match case?

with open('input.txt', 'r') as input:
    strategy_guide = input.read().splitlines()
    
    for throws in strategy_guide:

        # Initiate variable to track score for each round, resetting on each loop.
        round_score = 0
        
        # first, calculate point score for what I throw
        # (if throws[0] is 'A', is there a way to "map" that to a variable 'A' that contains the point value for rock?)
        if throws[2] == "X":
            round_score += rock
        elif throws[2] == "Y":
            round_score += paper
        else:
            round_score += scissors
        
        # next, calculate point score for win, loss, or draw
        if throws == "A Y" or throws == "B Z" or throws == "C X":
            round_score += win
        elif throws == "A X" or throws == "B Y" or throws == "C Z":
            round_score += draw
        else:
            round_score += loss

        # Add round score to total score
        total_score += round_score

print(total_score)