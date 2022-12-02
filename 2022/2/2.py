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
    
    for throw_wld in strategy_guide:

        # Initiate variable to track score for each round, resetting on each loop.
        round_score = 0
        
        # Check opponent's throw, then your win/loss/draw, and calculate your throw accordingly.
        if throw_wld[2] == "X":
            round_score += loss
            if throw_wld[0] == "A":
                round_score += scissors
            elif throw_wld[0] == "B":
                round_score += rock
            else:
                round_score += paper
        elif throw_wld[2] == "Y":
            round_score += draw
            if throw_wld[0] == "A":
                round_score += rock
            elif throw_wld[0] == "B":
                round_score += paper
            else:
                round_score += scissors
        else:
            round_score += win
            if throw_wld[0] == "A":
                round_score += paper
            elif throw_wld[0] == "B":
                round_score += scissors
            else:
                round_score += rock

        # Add round score to total score
        total_score += round_score

print(total_score)