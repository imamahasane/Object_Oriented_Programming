#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 04:41:15 2019

@author: imam
"""

try:
    print("Hello")
    print(1 / 0)

except ZeroDivisionError:
    print("Divided by zero")
    
finally:
    print("This code will run no matter what.")