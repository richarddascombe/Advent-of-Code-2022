# Advent of code 2022 day 1 part 2
# calory counting
# work out the calories carried by the elves with the 3 highest calory loads


with open(r"/Users/richard10998/Documents/Advent2022/calories.txt", "r") as cals:
    raw_data = cals.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
calories = raw_data.split('\n')

calcount=0
calmax=0
i=0
calcountlist=list()

# step through the list of elves' calorie gatherings
for c in calories:

    # each elf's calories are separated by a blank row (not a digit!)
    if c.isdigit():
        # sum the items in this elf's bag
        calcount=calcount + int(c)
    else:
        # we've reached the end of this elf's bag, stick it in a list of totals
        calcountlist.append(calcount)
        calcount=0

# sort the list of totals so we can find the 3 highest and sum them    
calcountlist.sort()
print('answer is ',calcountlist[-1]+calcountlist[-2]+calcountlist[-3])