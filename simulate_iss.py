import serial
import sys
import time
import urllib2

import json
import math
from random import randint
import utm
from  LatLongUTMconversion import * 

d_tmp_x = 26
d_tmp_y  = 'L'.lower()


all_letters = {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10, 'n': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15, 't': 16, 'u': 17, 'v': 18, 'w': 19, 'x': 10 }

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


def main():
	global d_tmp_x
	global d_tmp_y

	all_data = []

	with open('all_data.txt') as fp:
		for line in fp:
			if line != "":
				all_data.append(line.rstrip())
	for z in all_data:
		print z
		if len(z) == 3:
	   		x = int(z[:2])
	   		y = z[2].lower()
	   	else:
	   		x = int(z[0])
	   		y =  z[1].lower()
	   	print "x from data => " + str(x)
	   	print "y from data => " + str(y)

	   	if y != d_tmp_y:
		   	if all_letters[y] > all_letters[d_tmp_y]:
		   		move_up()
		   	else:
		   		move_down()
		   	d_tmp_y = y

   		
	   	if x != d_tmp_x:
	   		d_tmp_x = x
	   		move_right()
	   	#print "value of d_tmp_x => " + str(d_tmp_x)
		time.sleep(3)
				
main()
	
