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

def move_right():
	print "mov laser right"
	ser.write("r")

def move_left():
	print "mov laser left"
	ser.write("l")

def move_up():
	print "mov laser up"
	ser.write("u")

def move_down():
	print "mov laser donw"
	ser.write("d")


def setup_iss_position():
	all_letters = {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10, 'n': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15, 't': 16, 'u': 17, 'v': 18, 'w': 19, 'x': 10 }

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
   	x = 31
   	y = "M".lower()
   
   	print x,y

	print all_letters[y]
	print all_letters[start_point_y]

	nb_pas_y = abs(all_letters[start_point_y] - all_letters[y])
	for i in range(0,nb_pas_y + 1):
   		if all_letters[y] > all_letters[start_point_y]:
	   		move_up()
	   	else:
	   		move_down()
   		time.sleep(2)

	nb_pas_x = abs(start_point_x - x)
   	for i in range(0,nb_pas_x):
   		if x > start_point_x:
	   		move_right()
	   	else:
	   		move_left()
   		time.sleep(2)


def main():
	global d_tmp

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
   		move_right()
   	print d_tmp
	time.sleep(5)

setup_iss_position()



#while True:
#	main()
	