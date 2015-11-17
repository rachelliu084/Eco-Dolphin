import serial
import math
import time
import plotly.plotly as py
from plotly.graph_objs import *
from array import *

import avoid
import checkPoint
import cmdAgent
import getHeading
import getPosGraph
import getPosition
import isfloat 
import hover
import proximity
import resurface
import separateString
import setAcceleration
import setBoundary
import setPoint
import setTarget
import tolI



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
#Cp = measure battery

#loop counters

i = 0 #for file population (maximum: 100)
n = 0 #for IMU calibration (average acceleration)

#Serial communication definition and initialization
ser = serial.Serial(port, baud, timeout=1)
ser.open()
























   
#main code begins here
setBoundary.setBoundary(bounds[0],bounds[1],bounds[2])
response = cmdAgent.cmdAgent(PwrOn)
print "hi"
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
while i < 11:
   elapsetime+=time.clock()
   #check if destination has been reached
   if (location == destination) or (location > bounds):
        while difftime < 15:
           ser.write(Hover)
           difftime+=time.clock()
        #write to sonar
                #retreat
           resurface.resurface()
           response  = cmdAgent.cmdAgent(PwrOff)
   else:
                #check the state of the agent
        if response == "" or response == "Ready":
           getPosition.getPosition()

          # cmdAgent(Fwd)
          # time.sleep(1) 
         
           
          # cmdAgent(PwrOff)
           #cmdAgent(PwrOn)
           #print summ
           #getHeading()
           
           #calculate the change in position
           diff[0] = location[0] - prevlocation[0]
           diff[1] = location[1] - prevlocation[1]
           diff[2] = location[2] - prevlocation[2]
           maglocation = math.sqrt((math.pow(diff[0],2))+(math.pow(diff[1],2))+(math.pow(diff[2],2)))

           #reassign previous location to current location
           #prevlocation=location
           n+=1
          # if n>15:#average the acceleration
            #checkPoint()
#            toHeading()
        else:#add Ready, Abort, Override option
                print 'Not Ready'
                response = cmdAgent.cmdAgent(PwrOn)
   if(i == 10):
       p = i / 10
       #getPosGraph.getPosGraph(xgraphpos,ygraphpos,zgraphpos, p)
       print "graph printed"


  

   i+=1


