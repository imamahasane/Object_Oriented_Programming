# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:06:50 2019

@author: Imam Ahasan
"""

#a = "this is a string"
#a = a.split(" ")
#
#mm = "-"
#m = mm.join(a)
#print(m)

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line2 = "-"
    line22 = line2.join(line)
    return line22
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)