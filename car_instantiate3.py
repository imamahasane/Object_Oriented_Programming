# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:13:24 2020

@author: emama
"""

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    def start(self):
        print("Starting the engine.")
        
my_car = Car("Yonix BD", "Black")

print("Name of the car: ", my_car.name)
print("Color of the car: ", my_car.color)

my_car.start()