#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 4 part 1        https://adventofcode.com/2022/day/3
# sack checking for comon items (set theory)
#
import re
count=0
with open(r"/Users/richard10998/Documents/Advent2022/advent2022-day4-pt1.txt", "r") as assignments:
    raw_data = assignments.read()

# pop the list of calories into a list: an empty list item indicates the end of each elf's gatherings
asses = raw_data.split('\n')
for ass in asses:
#    a = ass.split(',')  # convert the assignments string into a couple of list items
    a = re.split(r',|-',ass)     # multiple delimiter split using the re.split method!!
    if (int(a[0])<=int(a[2]) and int(a[1])>=int(a[3])) or (int(a[2])<=int(a[0]) and int(a[3])>=int(a[1])):
        count=count+1
        print(a)

print('answer =',count)