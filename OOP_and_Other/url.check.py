# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:19:55 2019

@author: Imam Ahasan
"""

import requests

url = "http://subeen.com/allpost/"
#print(url)

response = requests.get(url)
print(response)

print(dir(response))
