# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:07:23 2020

@author: emama
"""

class Car:
    name = ''
    color = ''
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def start(self):
        print("Starting the engine.")
        
my_car  = Car("Corolla", "White")

print(my_car.name)
print(my_car.color)

my_car.start()