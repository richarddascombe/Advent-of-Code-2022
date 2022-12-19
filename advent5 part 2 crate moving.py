#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 5 part 2        https://adventofcode.com/2022/day/4
# tower of hanoi
#
ts=[[],['S','M','R','N','W','J','V','T'],
    ['B','W','D','J','Q','P','C','V'],
    ['B','J','F','H','D','R','P'],
    ['F','R','P','B','M','N','D'],
    ['H','V','R','P','T','B'],
    ['C','B','P','T'],
    ['B','J','R','P','L'],
    ['N','C','S','L','T','Z','B','W'],
    ['L','S','G']]
                                   

with open(r"/Users/richard10998/Documents/Advent2022/advent2022-day5-pt1.txt", "r") as hanoi:
    raw_data = hanoi.read()

rows=raw_data.split('\n')
# for each row of instructions, extract how many sacks to move from where to where
for i in range(10,len(rows)):
    r=rows[i].split()
    count=int(r[1])
    start=int(r[3])
    end=int(r[5])
    l=len(ts[start])
# in part 2 we move multiple sacks at once 
    for j in range(0,count):
        ts[end].append(ts[start][l-count])
        ts[start].pop(l-count)        

print('answer is',ts[1][-1],ts[2][-1],ts[3][-1],ts[4][-1],ts[5][-1],ts[6][-1],ts[7][-1],ts[8][-1],ts[9][-1])
print("but without the spaces")