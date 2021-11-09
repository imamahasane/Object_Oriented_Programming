# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 05:57:54 2019

@author: Imam Ahasan
"""

class Car:
    name = ""
    color = ""
    
    def start():
        print("Starting the car")
        
Car.name ="X ustha"
Car.color = "Black"
print("The nem of car : ",Car.name)
print("Color : ", Car.color)

Car.start()

print(dir(Car))