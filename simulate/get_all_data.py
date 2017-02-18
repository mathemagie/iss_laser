import serial
import sys
import time
import urllib2

import json
import math
from random import randint
import utm
from  LatLongUTMconversion import * 

d_tmp = ''


def get_iss_position():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	return obj['iss_position']['latitude'], obj['iss_position']['longitude']

def main():
	global d_tmp

	lat, lng = get_iss_position()
	lat = float(lat)
	lng = float(lng)
	print lat,lng
	(z, e, n) = LLtoUTM(23,lat, lng)
   	print z,e,n
   	if z != d_tmp:
   		d_tmp = z
   		print z
   		file = open("all_data.txt","a")
   		file.write(z + "\n") 
   		file.close()
 
	time.sleep(5)

while True:
	main()
	