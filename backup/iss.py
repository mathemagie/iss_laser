from __future__ import division
import serial
import time
import urllib2
import json
import math
from random import randint
import utm
from  LatLongUTMconversion import * 


#http://www.latlong.net/c/?lat=51.4084&long=85.0241

try:
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)   # open serial port that Arduino is using
except OSError:
	print "usb failed"

try:
	#ser.write("92")
	time.sleep(1) # delays for 5 seconds
	#ser.write("100")
	#time.sleep(5) # delays for 5 seconds
	#ser.write("105")

except:
	print "setup fail"

def get_iss_position():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())
	#print obj['iss_position']['latitude'], obj['iss_position']['longitude']
	return obj['iss_position']['latitude'], obj['iss_position']['longitude']


while 1:
	lat, lng = get_iss_position()
	lat = float(lat)
	lng = float(lng)
	print lat,lng
#	print utm.latitude_to_zone_letter(lat)
	#utm.from_latlon(lat,lng)
	#d = str(int(math.ceil(float(lng))))
	#print d
	#d = str(randint(10,179))
	#print d
	(z, e, n) = LLtoUTM(23,lat, lng)
   	print z,e,n
   	if len(z) == 3:
   		d = int(z[:2])
   	else:
   		d = int(z[0])
   	print d
   	a =  104 - ((39 / 60) * d) 
   	print a
   	b = str(int(a))
   	print b
   	#ser.write(b)
	time.sleep(5)

