# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:11:46 2019

@author: Imam Ahasan
"""

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    def start(self):
        print("Starting the engine")
        
my_car = Car("Corolla", "Red")
print(my_car.name)
print(my_car.color)
my_car.start()