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

cmd = ["r=10","u=20"]

for i in cmd:
	send_command(i)
	time.sleep(3)