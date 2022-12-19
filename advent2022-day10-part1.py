# Advent of code 2022 day 10 part 1
# Cathode-Ray Tube - clock cycles



with open(r"/Users/richard10998/Documents/Advent2022/advent2022-day10.txt", "r") as guide:
    raw_data = guide.read().strip().split('\n')
#with open(r"/Users/richard10998/Documents/Advent2022/DAY10TESTDATA.txt", "r") as guide:
#    test_data = guide.read().strip().split('\n')

l=[]
x=1
# for each instruction
for t in raw_data:
    if t=='noop':
        l.append(x) # only one clock cycle - no change in value
    else:  
        l.append(x) # 1st clock cycle - no change on the first cycle
        v=int(t.split(' ')[1])  # extract the value
        x+=v
        l.append(x) # 2nd clock cycle - new value

    
l20 = 20*l[18]
l60 = 60*l[58]
l100 = 100*l[98]
l140 = 140*l[138]
l180 = 180*l[178]
l220 = 220*l[218]

print('answer=',l20,'+',l60,'+',l100,'+',l140,'+',l180,'+',l220,'=',l20+l60+l100+l140+l180+l220)