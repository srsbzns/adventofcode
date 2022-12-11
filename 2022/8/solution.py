# count the number of trees that are visible from outside the grid when looking directly along a row or column.
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

# all edge trees are visible, as there's nothing between them and the edge

import numpy as np
from colorama import Cursor

# parse puzzle input.txt and return as a formatted list
def get_puzzle_input(filename):
    with open(filename, 'r') as file:
        formatted_input = file.read().splitlines()

        for count, string in enumerate(formatted_input):
            formatted_input[count] = [int(i) for i in string]

        return formatted_input

# create a new numpy array from formatted input
def generate_grid(formatted_input):
    grid = np.asarray(formatted_input)

    return grid


grid = generate_grid(get_puzzle_input('input.txt'))

# if the index position of the tree is 0 or len() it's visible
# if the tree height is the max in the following slices, it's visible:
#   it's own index position to the end of axis 0
#   it's own index position to the beginning of axis 0
#   it's own index position to the end of axis 1
#   it's own index position to the beginning of axis 1

visible_trees = 0

for x, row in enumerate(grid):
    for y, tree in enumerate(row):

        # identify if the tree is an edge tree
        if x == 0 or y == 0 or x == len(row)-1 or y == len(grid)-1:
            visible_trees += 1
       
        # identify if tree is the largest tree along the x axis between itself and the west edge
        elif tree > max(grid[x, 0:y]):
            visible_trees += 1

        # identify if tree is the largest tree along the x axis between itself and the east edge
        elif tree > max(grid[x, y+1:]):
            visible_trees += 1
        
        # identify if tree is the largest tree along the y axis between itself and the north edge
        elif tree > max(grid[0:x, y]):
            visible_trees += 1

        # identify if tree is the largest tree along the y axis between itself and the south edge
        elif tree > max(grid[x+1:, y]):
            visible_trees += 1

print(visible_trees)

current_best = 0

for x, row in enumerate(grid):
    for y, tree in enumerate(row):

        # identify if the tree is an edge tree
        if x == 0 or y == 0 or x == len(row)-1 or y == len(grid)-1:
            pass
        else:
            
            # reset score placeholders
            tree_score = []

            # get all sightlines for tree
            sightlines = [grid[x, 0:y], grid[x, y+1:], grid[0:x, y], grid[x+1:, y]]
            
            for direction in sightlines:
                directional_score = 0
                counter = 0
                while counter < len(direction) and direction[counter] < tree:
                    directional_score += 1
                    counter += 1
                directional_score += 1

                tree_score.append(directional_score) 

            if current_best < np.prod(tree_score):
                current_best = np.prod(tree_score)

print(current_best)