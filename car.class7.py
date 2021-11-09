# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:31:45 2019

@author: Imam Ahasan
"""

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    def start(self):
        print("Name : ", self.name)
        print("Color : ", self.color)
        print("Starting the engine")
        
my_car = Car("Appachi", "Red")
my_car.start()