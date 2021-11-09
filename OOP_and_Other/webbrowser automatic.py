# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 02:17:30 2020

@author: emama
"""

import requests
import os
import webbrowser as wb

url = "http://www.subeen.com/allposts/"

response = requests.get(url)

with open("dimik.html", "w", encoding = response.encoding) as f:
    f.write(response.text)
    
file_path = os.path.realpath("dimik.html")
print(file_path)

wb.open("file://" + file_path)