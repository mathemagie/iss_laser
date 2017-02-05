import serial
import sys
import time


try:
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)   # open serial port that Arduino is using
except OSError:
	print "usb failed"

#angle = sys.argv[1]
#print "angle =>"  + angle	
#ser.write(angle)

while 1:
	for i in range(900,700,-11) :
		ser.write(str(i))
		print i
		time.sleep(2)
