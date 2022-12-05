with open('input.txt', 'r') as input:
    packing_list = input.read().splitlines()


# each line = the contents of both rucksack's compartments
# get total number of characters in line, then divide by 2.
# line[0:number-1:1] = compart 1, line [number:number*2] = compart 2s

compartments_inventory = []

# format the input into something usable
for i in packing_list:

    # determine how many items are in each rucksack (assuming each rucksack has 2 evenly-full compartments)
    split = int(len(i)/2)

    # create a set from the inventory of compartment 1
    compart1 = set(i[0:split:1])
    # create a set from the inventory of compartment 2
    compart2 = set(i[split::1])

    # create a list object with the inventories of both compartments
    compartments = [compart1, compart2]

    # append the list object to a running list of the inventories of every rucksack's compartmental inventories
    compartments_inventory.append(compartments)

# for each rucksack, find which item types (letters) are present in both compartments, figure out a "point" value for that rucksack, and then sum the point 
# value into a running total (the "opportunity cost")
opportunity_cost = 0
# Lowercase item types a through z have priorities 1 through 26.
a = ord('a')    
# Uppercase item types A through Z have priorities 27 through 52.
A = ord('A')

for i in compartments_inventory:
    overlap_items = i[0].intersection(i[1])

    # Iterate through the resultant set of "overlap" items and for each item type found, sum the "priority" of the item type.
    for item_type in overlap_items:
        if item_type.islower():
            opportunity_cost += ord(item_type) - a + 1
        else:
            opportunity_cost += ord(item_type) - A + 27

print(opportunity_cost)