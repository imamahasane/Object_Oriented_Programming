# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:09:43 2019

@author: Imam Ahasan
"""

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    def start(self):
        print("Starting the engine!")
        
my_car = Car("BMW", "White")
my_car.year = 2018
my_car.cc = 5001

print("Name:",my_car.name, "\nColor:",my_car.color, "\nYear:", my_car.year, "\nCC:",my_car.cc)