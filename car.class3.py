# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 06:21:53 2019

@author: Imam Ahasan
"""

class Car:
    name = ""
    color = ""
    
    def start():
        print("Starting the car engine")
        
#Creating a car object
my_car = Car()
my_car.name = "U ustha"
print(my_car.name)
my_car.start()