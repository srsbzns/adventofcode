# add numbers until you hit blank line
# each line is either a number, or a blank line (which is effectively just a delimiter)

# does CSV-style input management come into play here? 

# what about a 2-dimensional array of some kind? (x = elf, y = total calories after summing all items in the list)

# how to extend this for future use? should I focus on building out an input processor of some kind?



elf_calories = []
calories_held = 0

# is there some way to validate input? make sure that a .txt being fed in is actually "valid?" 
# the following assumes that the elves are delimited by line breaks, except at the end, where the last elf's list
# simply ends at EOF
with open('input.txt', 'r') as file:
  for line in file.readlines():
    if line != "\n":
      calories_held += int(line.rstrip('\n'))
    else:
      elf_calories.append(calories_held)
      calories_held = 0
  elf_calories.append(calories_held)
      
print(max(elf_calories))