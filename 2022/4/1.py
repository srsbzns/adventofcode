# every section has a unique ID number (section_id)

# each elf is assigned a range of section_ids

# each line of input (2-4,6-8) represents a comma-delimited list of each elf's assigned range of section_ids.

# Some of the pairs have noticed that one of their assignments fully contains the other (e.g. one is a subset of the other)

# In how many assignment pairs does one range fully contain the other?

with open('input.txt', 'r') as file:
    assigned_ranges = file.read().splitlines()

    subset_count = 0

    # For each line: split the line at the comma(s) to get each elf's individual assigned range and create sets for each individual elf containing the range.
    for line in assigned_ranges:
        group_assignments = line.split(',')

        group_ranges = []

        for hypenated_range in group_assignments:
            # get the hyphenated range and find your lower + upper boundaries so you can generate a full range between for creating a set
            lower_bound = int(hypenated_range.split('-')[0])
            upper_bound = int(hypenated_range.split('-')[1]) + 1

            # get the full range of numbers between the bounds, create a set from them, and add that elf's full range of assigned sections to the group's list
            group_ranges.append(set(range(lower_bound,upper_bound)))

        # check if either elf's assigned range is a subset of the others
        if group_ranges[0] <= group_ranges[1] or group_ranges[1] <= group_ranges[0]:
            subset_count += 1

print(subset_count)