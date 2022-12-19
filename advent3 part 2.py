#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 3 part 2        https://adventofcode.com/2022/day/3
# sack checking for comon items (set theory)
#


with open(r"/Users/richard10998/Documents/Advent2022/rucksacks.txt", "r") as rucksacks:
    raw_data = rucksacks.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
sacks = raw_data.split('\n')
prioritysum=0


# scan eack group of 3 sacks for a common item (using set intersection method)
for i in range(0,len(sacks),3):
    s = sacks[i]
    set1=set(sacks[i])
    set2=set(sacks[i+1])
    set3=set(sacks[i+2])
    set4 = set3.intersection(set1.intersection(set2))
    commmon_item=set4.pop() # the only way to access the set item is by using pop()!!!!!
    
    if ord(commmon_item)<=90:
        prioritysum = prioritysum + ord(commmon_item) - 38

    else:
        prioritysum = prioritysum + ord(commmon_item) - 96

print('answer is ',prioritysum)
