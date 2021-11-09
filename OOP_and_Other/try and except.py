#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 03:49:00 2019

@author: imam
"""

try:
    a = 1000
    b = int(input("Enter a divisor to divide 1000: "))
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted!")
    
