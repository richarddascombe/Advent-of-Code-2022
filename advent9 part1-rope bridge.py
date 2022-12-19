#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 9        https://adventofcode.com/2022/day/9
# Rope Bridge
#              

def chunks(lst, n):
    """break a list into chunks (sublists)."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

""" find the postion of the tail of the rope give its start point and the head position """
def findtpos(t,h):
    dx = h[0]-t[0]  # delta x
    dy = h[1]-t[1]  # delta y
    if (abs(dx) <= 1) and (abs(dy) <=1):
        # touching - no need to do anything
        return(t)
    # the following algorithm took a bit of thinking but try it out on a paper grid
    # BTW dx/abs(dx) yields -1 if dx < 0 and 1 if dx > 0
    if abs(dx)>1:
        t[0]+=int(dx/abs(dx))
        if abs(dy)>0: 
            t[1]+=int(dy/abs(dy))
        return(t)
    if abs(dy)>1:
        t[1]+=int(dy/abs(dy))
        if abs(dx)>0:
            t[0]+=int(dx/abs(dx))
        return(t)
    
    return(t)

with open(r"/Users/richard10998/Documents/Advent2022/advent2022-day9.txt", "r") as lines:
    motions = lines.read().strip().split()

mot=list(chunks(motions,2)) # split the list into a list of coordinates
# test data below - DELETE -
#mot=[['R','4'],['U','4'],['L','3'],['D','1'],['R','4'],['D','1'],['L','5'],['R','2']]

hpos=[0,0]  # the head of the rope starts at [0,0]
tpos=[0,0]  # so does the tail
position_set=set()  # positions visted by the tail

# for each motion work out the head position ... step by step
for m in mot:
    distance=int(m[1])
    if m[0]=='L':
        for i in range(distance):   # move left step by step
            hpos[0]-=1
            tpos = findtpos(tpos,hpos)      # work out where the tail will be
            position_set.add(tuple(tpos))   # add each position visited by the tail to a set
    elif m[0]=='R':
        for i in range(distance):
            hpos[0]+=1
            tpos = findtpos(tpos,hpos)
            position_set.add(tuple(tpos))

    elif m[0]=='U':
        for i in range(distance):
            hpos[1]+=1
            tpos = findtpos(tpos,hpos)
            position_set.add(tuple(tpos))
            
    elif m[0]=='D':
        for i in range(distance):
            hpos[1]-=1 
            tpos = findtpos(tpos,hpos)
            position_set.add(tuple(tpos))
            
print('answer=', len(position_set)) # answer is the number of unique positions visted by the tail

