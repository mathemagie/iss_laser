import serial
import sys
import time

try:
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)   # open serial port that Arduino is using
except OSError:
	print "usb failed"
	#sys.exit()

def send_command(command=""):
	ser.write(command)

while True:
	mydata = raw_input('command to send to LASER => ')
	d = str(mydata)
	print d
	send_command(d)
	time.sleep(1)