import serial
import sys
import time
import urllib2

import json
import math
from random import randint
import utm
from  LatLongUTMconversion import * 

d_tmp = '0'

start = 900
end = 700

tmp_start = start

try:
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)   # open serial port that Arduino is using
except OSError:
	print "usb failed"
	#sys.exit()

def change_pos_laser(command="f"):
	#global tmp_start
	print "mov laser"
	#ser.write(str(i))
	#print tmp_start
	#i = int(tmp_start) - 11;
	#print i
	#tmp_start = i
	ser.write(command)

def send_command(command=""):
	print "change direction"
	ser.write(command)



def get_iss_position():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	return obj['iss_position']['latitude'], obj['iss_position']['longitude']

while True:
	mydata = raw_input('Prompt :')
	d = str(mydata)
	send_command(d)
#  	if d == d_tmp:
 # 		print "------"
  #	else:
   #		d_tmp = d
   		#change_pos_laser()
	time.sleep(1)