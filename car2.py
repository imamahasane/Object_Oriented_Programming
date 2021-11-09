# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:20:45 2020

@author: emama
"""

class Car:
    name = ""
    color = ""
    
    def start():
        print("Starting the engine.")
        
Car.name = "Axio"
Car.color = "Black"

print("Name of the car:", Car.name)
print("Color:", Car.color)

Car.start()

#print(dir(Car))