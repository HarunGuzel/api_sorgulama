# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:14:12 2022

@author: Hg
"""
#Harun Güzel 02195076060

import requests

URL = "https://dog.ceo/api/breeds/image/random"

result = requests.get(URL)

data = result.json()

print(data)



