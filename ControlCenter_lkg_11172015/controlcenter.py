#Eco-Dolphin
#Control center for the decision making interface. 
#Each imported function will support the node output in some capacity.

import serial
import math
import time

fob = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/accel.txt','w')
fob2 = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/ylocation.txt','w')
port = '/dev/ttyACM0'
baud = 4800
response = ""

#commands to agent
Accel = '1'
PwrOn = '2'
PwrOff = '3'
Idle = '4'
Right = '5'
Left = '6'
Rise = '7'
Dive = '8'
Fwd = '9'
Back = '0'

