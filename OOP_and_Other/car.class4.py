# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 06:32:06 2019

@author: Imam Ahasan
"""

class Car:
    name = "        #Class attribute
    color = ""
    
    def start(self):
        print("Starting the car engine")
        
#Creating a car object
my_car = Car()
my_car.name = "U ustha"
print(my_car.name)
my_car.start()