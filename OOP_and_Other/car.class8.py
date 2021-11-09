# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:54:54 2019

@author: Imam Ahasan
"""

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    def start(self):
        print("Brand Name: ",self.name)
        print("Color: ", self.color)
        print("Starting The engine\n")
        
        
my_car = Car("BD Ustha", "yelloo")
my_car.start()

my_car2 = Car("Apachi", "Red")
my_car2.start()

my_car3 = Car("Fz", "White")
my_car3.start()