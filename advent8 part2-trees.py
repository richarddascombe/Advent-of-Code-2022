#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 8 part 2        https://adventofcode.com/2022/day/6
# comms device - wood for the trees - which trees have the best view
#
import numpy as np                 

with open(r"/Users/richard10998/Documents/Advent2022/advent2022-day8.txt", "r") as forest:
    lines = forest.read().strip().split()
# test data below - DELETE -
lines=['30373','25512','65332','33549','35390']

rows= [list(map(int, list(line))) for line in lines]
    
nr=np.array(rows)

perimeter_length = len(nr)*2 + len(nr[0])*2 - 4

ans = 0

# now step through each tree - except the ones on the perimeter which we know are visible
for i in range(1,len(lines)-1):
    for j in range(1,len(lines[0])-1):
        tree_height = nr[i][j]
        scenic_score=1

# all the trees on the perimeter are visible from outside the forest so add them in            
ans = ans + perimeter_length

print('answer is',ans)
