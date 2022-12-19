# Advent of code 2022 day 1 part 1
# counting elves' calories



with open(r"/Users/richard10998/Documents/Advent2022/calories.txt", "r") as cals:
    raw_data = cals.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
calories = raw_data.split('\n')

calcount=0
calmax=0
i=0

# step through the list of elves' calorie gatherings
for c in calories:


    # each elf's calories are separated by a blank row (not a digit!)
    if c.isdigit():
        # sum the items in this elf's bag
        calcount=calcount + int(c)
    else:
        # we've reached the end of this elf's bag, check if it's the biggest & record if so
        if calcount>calmax:
            calmax=calcount
        calcount=0
    
print('answer is ',calmax)