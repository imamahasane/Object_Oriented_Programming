#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 05:44:31 2019

@author: imam
"""

print("Hello")
raise NameError("HiThere")

raise TypeError

try:
    num = 5 / 0
except:
    print("Custom message")
    raise