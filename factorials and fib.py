#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:37:18 2022

@author: richard10998
"""

def fact(x):
    if x in [0,1]: 
        return x
    else:
        return(x*fact(x-1))



def fib(x):
        if x in [0,1]: 
            return x
        else: 
            return(x+fib(x-1))