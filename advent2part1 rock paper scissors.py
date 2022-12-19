# Advent of code 2022 day 2 part 1
# Rock paper scissors



with open(r"/Users/richard10998/Documents/Advent2022/encrypted_strategy_guide.txt", "r") as guide:
    raw_data = guide.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
turns = raw_data.split('\n')
score = 0

# for each turn see what each player plays and score accordingly
for t in turns:
    if t[2]=='X':       # I play rock
        score=score+1
        if t[0]=='A': score=score+3     # he plays rock = draw
        if t[0]=='C': score=score+6     # he plays scissors = win
        
    if t[2]=='Y':       # I play paper
        score=score+2
        if t[0]=='A': score=score+6     # he plays rock = win
        if t[0]=='B': score=score+3     # he plays paper = draw
        
    if t[2]=='Z':       # I play scissors
        score=score+3
        if t[0]=='B': score=score+6     # he plays paper = win
        if t[0]=='C': score=score+3     # he plays scissors = draw

    print(t,score)

print('answer is ',score)