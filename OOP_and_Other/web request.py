# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:20:42 2020

@author: emama
"""

import requests

url = "http://www.subeen.com/allposts/"

response = requests.get(url)
print(response)

print(type(response))

attibute = dir(response)
print(attibute)
