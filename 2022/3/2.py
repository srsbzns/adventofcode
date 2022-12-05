with open('input.txt', 'r') as input:
    packing_list = input.read().splitlines()

compartments_inventory = []

# split each rucksack into it's separate compartments
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

badge_cost = 0

elf_group_inventory = []

# find intersection between rucksacks in packing_list in 3-rucksack increments, e.g. packing_list[0].intersection(packing_list[1],packing_list[2])
for count, rucksack_inventory in enumerate(packing_list):
    if (count + 1) % 3 != 0:
        elf_group_inventory.append(set(rucksack_inventory))
    else:
        elf_group_inventory.append(set(rucksack_inventory))
        badge_item_type = elf_group_inventory[count] & elf_group_inventory[count-1] & elf_group_inventory[count-2]
        for item_type in badge_item_type:
            if item_type.islower():
                badge_cost += ord(item_type) - a + 1
            else:
                badge_cost += ord(item_type) - A + 27

print(badge_cost)