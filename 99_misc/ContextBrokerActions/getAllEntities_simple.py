# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:59:23 2015

@author: sgr
"""
import requests


#curl 127.0.0.1:1026/v1/contextEntities -X GET -s -S --header 'Content-Type: application/json' --header 'Accept: application/json'




url    = "http://137.226.75.120:1026/v1/contextEntities"
header = {"Content-Type" : "application/json", "Accept" : "application/json"}


returnValue = requests.get(url = url, headers = header)
print(returnValue)



