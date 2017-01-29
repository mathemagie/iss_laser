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

try:
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)   # open serial port that Arduino is using
except OSError:
	print "usb failed"
	sys.exit()

def get_iss_position():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	return obj['iss_position']['latitude'], obj['iss_position']['longitude']

while True:
	lat, lng = get_iss_position()
	lat = float(lat)
	lng = float(lng)
	print lat,lng
	(z, e, n) = LLtoUTM(23,lat, lng)
   	print z,e,n
   	if len(z) == 3:
   		d = int(z[:2])
   	else:
   		d = int(z[0])
   	print d
   	if d != d_tmp:
   		d_tmp = d
   		ser.write("f")
		print "mov laser"
   	print d_tmp
	time.sleep(5)