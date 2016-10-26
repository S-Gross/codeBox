#!/usr/bin/env python
import requests


entity = "BeispielEntity"
name   = "EinName"
value  = "EinValue"

url    = "http://137.226.75.89:1026/ngsi10/contextEntities/"
header = {"Content-Type" : "application/json", "Accept" : "application/json"}
data = {u'attributes' : [{u'name' : name, u'value': value}]}

returnValue = requests.post(url = url + entity, headers = header, json = data)
print(returnValue)



