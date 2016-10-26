#!/usr/bin/env python
import requests
import sys

if len(sys.argv) == 2:
	entity = sys.argv[1]
	url = "http://137.226.75.89:1026/ngsi10/contextEntities/"

	r = requests.get(url=url+entity,
			 headers={"Content-Type":"application/json", "Accept":"application/json"})

	print "Request resulted in: "
	print r
	print r.text
	print 

	result = r.json()

	print "Current status: " + str(result['contextElement']['attributes'][2]['value'])
else:
	print "Usage: python get.py entity"
