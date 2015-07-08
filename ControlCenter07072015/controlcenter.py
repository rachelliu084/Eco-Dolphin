import serial
import math
import time
import plotly.plotly as py
from plotly.graph_objs import *
from array import *

# Global variables defined as follows
fob = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/accel.txt','w')
fob2 = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/ylocation.txt','w')
port = '/dev/ttyACM0'
baud = 57600
response = ''

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


#tracking variables
bounds = [20.0,20.0,10.0]
bed = [0.0,0.0,0.0]
targetangle = [0.0,0.0,0.0]
angle = [0.0,0.0,0.0]
heading = [0.0,0.0,0.0]
acceleration = [0.0,0.0,0.0]
destination = [12.0,12.0,5.0]
location = [0.0,0.0,0.0]
prevlocation = [0.0,0.0,0.0]
prevaccel=[0.0,0.0,0.0]
prevangle = [0.0,0.0,0.0]
prevtime = time.clock()
Gyro = '7'
tolerance = 2.0
elapsetime = 0.0
summ = [0,0,0]
diff = [0,0,0]
diffaccel = [0.0,0.0,0.0]
diffgyro = [0.0,0.0,0.0]
xgraphpos = list()
ygraphpos = list()
zgraphpos = list()
#main code begins here
setBoundary(bounds[0],bounds[1],bounds[2])
response = cmdAgent(PwrOn)
print response
difftime = time.clock() + prevtime
#stringtime = str(difftime)
#local variables
endx = 0
beginy = 0
endy = 0
beginz = 0
endz = 0
#functional loop
while 1:
   elapsetime+=time.clock()
   #check if destination has been reached
   if (location == destination) or (location > bounds):
        while difftime < 15:
           ser.write(Hover)
           difftime+=time.clock()
        #write to sonar
                #retreat
           resurface()
           response  = cmdAgent(PwrOff)
   else:
        #check the state of the agent
        if response == "" or response == 'Ready':
           getPosition()

           #cmdAgent(Fwd)
           #time.sleep(3)

        elif response == 'Interrupt':#add Ready, Abort, Override option
	    #chkoverride()
        else:	
           print 'Not Ready'
           response = cmdAgent(PwrOn)


   i+=1
