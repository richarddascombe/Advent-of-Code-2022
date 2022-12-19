#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 5 part 1        https://adventofcode.com/2022/day/4
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




for i in range(10,len(rows)):
    r=rows[i].split()
    count=int(r[1])
    start=int(r[3])
    end=int(r[5])
    
    for x in range(1,10):
        print(x,ts[x])

    print(r)
    

        
    for j in range(0,count):
        ts[end].append(ts[start].pop())
    print('MOVED ')

for x in range(1,10):
    print(x,ts[x])

print('answer is',ts[1][-1],ts[2][-1],ts[3][-1],ts[4][-1],ts[5][-1],ts[6][-1],ts[7][-1],ts[8][-1],ts[9][-1])
