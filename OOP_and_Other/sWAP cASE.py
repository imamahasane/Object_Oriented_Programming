# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 06:26:41 2019

@author: Imam Ahasan
"""

def swap_case(s):
    re = s.swapcase()
    return re

if __name__ == '__main__':
    S = input()
    result = swap_case(S)
    print(result)
    