#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:19:51 2022

@author: richard10998
"""

# Advent of code 2022 day 6 part 1        https://adventofcode.com/2022/day/6
# comms device - parsing
# 
                       

with open(r"/Users/richard10998/Documents/Advent2022/advent2022-day6-part-1.txt", "r") as datastream:
    raw_data = datastream.read()

    for i in range(0,len(raw_data)-14):
        print(raw_data[i:i+14])
        if len(set(raw_data[i:i+14]))==14:   # sneaky use of sets to identify dupicate characters
            break
print('answer is',i+14)
