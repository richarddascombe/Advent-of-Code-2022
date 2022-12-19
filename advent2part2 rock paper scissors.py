# Advent of code 2022 day 2 part 2 
# Rock paper scissors




with open(r"/Users/richard10998/Documents/Advent2022/encrypted_strategy_guide.txt", "r") as guide:
    raw_data = guide.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
turns = raw_data.split('\n')
score = 0

# for each turn, see what he plays and decide what i need to play.....
for t in turns:
    if t[2]=='X':       # I need to lose
        
        if t[0]=='A': score=score+3     # he plays rock so i play scissors (3)
        if t[0]=='B': score=score+1     # he plays paper so i play rock (1)
        if t[0]=='C': score=score+2     # he plays scissors i play paper (2)
        
    if t[2]=='Y':       #  I need to draw
        score=score+3
        if t[0]=='A': score=score+1     # he plays rock so i play rock (1)
        if t[0]=='B': score=score+2     # he plays paper so i play paper (2)
        if t[0]=='C': score=score+3     # he plays scissors i play scissors (3)
        
    if t[2]=='Z':       # I need to win
        score=score+6
        if t[0]=='A': score=score+2     # he plays rock so i play paper (2)
        if t[0]=='B': score=score+3     # he plays paper so i play scissors (3)
        if t[0]=='C': score=score+1     # he plays scissors i play rock (1)

print('answer is ',score)