#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 04:02:34 2019

@author: imam
"""

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)

except ZeroDivisionError:
    print("Divided by Zero, It's not permitted!")
except (ValueError, TypeError):
    print("Value or Type error occurred")