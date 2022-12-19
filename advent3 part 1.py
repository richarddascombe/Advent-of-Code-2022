#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 3 part 1
# sack checking          https://adventofcode.com/2022/day/3
# 


with open(r"/Users/richard10998/Documents/Advent2022/rucksacks.txt", "r") as rucksacks:
    raw_data = rucksacks.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
sacks = raw_data.split('\n')
prioritysum=0


# scan eack sack
for s in sacks:
    l = len(s)
    match = False
    for i in range(0,int(l/2)):    # for each item in the first compartment of the sack
        if s[int(l/2):].find(s[i]) != -1: # see if it's also in the 2nd compartment
            # if a character is found in both the first half of the string and the 2nd half then 
            # add it's priority
            match=True     # we don't actually need to check for 'no match found' but helped debug
            if ord(s[i])<=90:
                prioritysum = prioritysum + ord(s[i]) - 38
                print(s[i],ord(s[i]) - 38,prioritysum)
            else:
                prioritysum = prioritysum + ord(s[i]) - 96
                print(s[i],ord(s[i]) - 96,prioritysum)
            break     # there's only 1 duplicate in each sack so having found it exit the inner loop
    if not match: print("NO MATCH",s)

print('answer is ',prioritysum)
