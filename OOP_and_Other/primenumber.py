# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 03:27:20 2019

@author: emama
"""

s = int(input())

for i in range(2, s):
    if s % i == 0:
        print(s, "is Not a prime number!!!")
        break
        
else:
    print(s, "is aprime number")
        