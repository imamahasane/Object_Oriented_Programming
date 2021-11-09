# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 05:33:15 2019

@author: Imam Ahasan
"""

class Car:
    name = "Premio"
    color = "white"
    
    def start():
        print("Starting the engine")
        
print("Name of the car : ",Car.name)
print("Color : ",Car.color)
Car.start()