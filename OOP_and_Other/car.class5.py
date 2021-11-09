# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 06:39:35 2019

@author: Imam Ahasan
"""

class Car:
    name = ""
    color = ""
    
    def __init__(self, name, color):
        self.name = name        #instance attribute
        self.color = color
        
    def start(self):
        print("Starting the engine")
        
my_car = Car("Corolla", "Whith")
print(my_car.name)
print(my_car.color)
my_car.start()

