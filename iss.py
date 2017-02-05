import serial
import sys
import time
import urllib2

import json
import math
from random import randint
import utm
from  LatLongUTMconversion import * 

d_tmp_x = ''
d_tmp_y  = ''

all_letters = {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10, 'n': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15, 't': 16, 'u': 17, 'v': 18, 'w': 19, 'x': 10 }

simulate = 0


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

def move_right(nb_step=5):
	print "mov laser right :  " + str(nb_step) 
	if not simulate: ser.write("r=" + str(nb_step)) 

def move_left(nb_step=5):
	print "mov laser left : " + str(nb_step)
	if not simulate: ser.write("l=" + str(nb_step)) 

def move_up(nb_step=7):
	print "mov laser up : " + str(nb_step)
	if not simulate: ser.write("u=" + str(nb_step))

def move_down(nb_step=7):
	print "mov laser down : " + str(nb_step)
	if not simulate: ser.write("d=" + str(nb_step))


def setup_iss_position():

	global d_tmp_x
	global d_tmp_y

	
	global y


	start_point_x = 30
	start_point_y = 'N'.lower()
	lat, lng = get_iss_position()
	lat = float(lat)
	lng = float(lng)
	print lat,lng
	(z, e, n) = LLtoUTM(23,lat, lng)
	print z,e,n
	if len(z) == 3:
   		x = int(z[:2])
   		y =str(z[2])
   	else:
   		x = int(z[0])
   		y = str(z[1])
   	y= y.lower()
   	#for testing
   	#x = 31
   	#y = "m".lower()
   
   	print x,y

   	d_tmp_x = x
   	d_tmp_y = y

	print all_letters[y]
	print all_letters[start_point_y]

	nb_pas_y = abs(all_letters[start_point_y] - all_letters[y])
	for i in range(0,nb_pas_y + 1):
   		if all_letters[y] > all_letters[start_point_y]:
	   		move_up()
	   	else:
	   		move_down()
   		time.sleep(1)

	nb_pas_x = abs(start_point_x - x)
   	for i in range(0,nb_pas_x):
   		if x > start_point_x:
	   		move_right()
	   	else:
	   		move_left()
   		time.sleep(1)


def main():
	global d_tmp_x
	global d_tmp_y

	lat, lng = get_iss_position()
	lat = float(lat)
	lng = float(lng)
	#print lat,lng
	(z, e, n) = LLtoUTM(23,lat, lng)
   	#print z,e,n
   	print "================================== " + z

	if len(z) == 3:
   		x = int(z[:2])
   		y = z[2].lower()
   	else:
   		x = int(z[0])
   		y =  z[1].lower()

   	if d_tmp_x == '':d_tmp_x = x
   	if d_tmp_y == '':d_tmp_y = y

   	print "x from data => " + str(x)
   	print "y from data => " + str(y)
   	print "tmp x from data => " + str(d_tmp_x)
   	print "tmp y from data => " + str(d_tmp_y)

   	#special case return to the  left  
   	if x == 1 and d_tmp_x == 60:
   		move_left(280)
   		d_tmp_x = 1
   		d_tmp_y = y.lower()
   		time.sleep(8)
   	else:
	   	if y != d_tmp_y:
		   	if all_letters[y] > all_letters[d_tmp_y]:
		   		move_up()
		   	else:
		   		if x > 43: step = 6
		   		move_down(step)
		   	d_tmp_y = y
	   	
	   	if x != d_tmp_x:
	   		d_tmp_x = x
	   		step = 5
	   		if x > 50: step = 4
	   		if x > 52: step = 3
	   		if x > 1 and x < 28: step = 4
	   		if x > 30  and x < 43: step = 4
	   		if x > 44  and x < 50: step = 4
	   		if x > 47  and x < 50: step = 5
	   		if x > 49: x = 4
	   		move_right(step)
		time.sleep(4)

#setup_iss_position()

try: 
	while True:
		main()
except KeyboardInterrupt:
	print "finito"
	