import serial
import sys
import time


try:
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)   # open serial port that Arduino is using
except OSError:
	print "usb failed"

#angle = sys.argv[1]
#print "angle =>"  + angle	
#ser.write("f")

while True:
	ser.write("f")
	print "mov laser"
	time.sleep(10) # delays for 5 seconds
	