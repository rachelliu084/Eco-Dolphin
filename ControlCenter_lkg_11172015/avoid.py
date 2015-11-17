#include <stdio.h>
import serial
import fgets
import cmdAgent
from array import*
port = '/dev/ttyACM0'
baud = 57600

ser = serial.Serial(port, baud, timeout=1)
ser.open()
location = 0
yedp = list()
maxnumber = 30


def avoid():
	global location
	yedp(30)
	with open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/position.txt' , 'r') as
	positionfile
	data = postionfile.readline()
	
	if location-data < tol:
	    if location[2] < data[2]:
                   cmdAgent.cmdAgnet(dive)

	    else :
	           cmdAgent.cmdAgent(rise)


#fclose(f)
