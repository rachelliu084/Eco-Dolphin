import cmdAgent
import separateString
import math
#import isfloat
import time
from array import *
import serial

port = '/dev/ttyACM0'
baud = 57600

fob = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/accel.txt','w')
fob2 = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/ylocation.txt','w')

ser = serial.Serial(port, baud, timeout=1)
ser.open()

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
response = ''

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
summ = [0,0,0]
diff = [0,0,0]
diffaccel = [0.0,0.0,0.0]
diffgyro = [0.0,0.0,0.0]
xgraphpos = list()
ygraphpos = list()
zgraphpos = list()
def isfloat(value):
        try:
                float(value)
                return True
        except ValueError:
                return False

def getPosition():
    global acceleration
    global location

    global prevaccel
    global diffaccel
    global response
    global prevlocation
    global summ
	  
    global xgraphpos
    global ygraphpos
    global zgraphpos
    #get the acceleration and separate string
    cmdAgent.cmdAgent(PwrOn)
    response = cmdAgent.cmdAgent(Accel)
    print "hi2"
    print response
    accelstring = separateString.separateString(response)
    print "hi3"
    if isfloat(accelstring[0]) and isfloat(accelstring[1]) and isfloat(accelstring[2]):
    #convert and assign acceleration values

        accelx = float(accelstring[0])
        accely = float(accelstring[1])
        accelz = float(accelstring[2])
        acceleration = [accelx,accely,accelz]
        print "acceleration"
        print acceleration

    #record the acceleration in a file
        fob.write('Accel: ')
        fob.write('%03d, ' % acceleration[0])
        fob.write('%03d, ' % acceleration[1])
        fob.write('%03d\n' % acceleration[2])

    #calculate the change in acceleration
        diffaccel[0] = acceleration[0] - prevaccel[0]
        diffaccel[1] = acceleration[1] - prevaccel[1]
        diffaccel[2] = acceleration[2] - prevaccel[2]
        magaccel = math.sqrt((math.pow(diffaccel[0],2))+(math.pow(diffaccel[1],2))+(math.pow(diffaccel[2],2)))

    #assign previous acceleration to the current acceleration
        prevaccel = acceleration

    #establish current location
        location[0] = 0.5*diffaccel[0]*math.pow(difftime,2)
        location[1] = 0.5*diffaccel[1]*math.pow(difftime,2)
        location[2] = 0.5*diffaccel[2]*math.pow(difftime,2)
    #the vector summ shows the position
        summ[0] += location[0] + prevlocation[0]
        summ[1] += location[1] + prevlocation[1]
        summ[2] += location[2] + prevlocation[2]
        print "This is position"
        print summ

    #assign previous location to current location
        summ = prevlocation

    #publish location and elapsed time to file server
        fob2.write('Place/Time: ')
        fob2.write('%03d, ' % summ[0])
        fob2.write('%03d, ' % summ[1])
        fob2.write('%03d, ' % summ[2])
        fob2.write('%03d\n' % elapsetime)

        xgraphpos.append(summ[0])
        ygraphpos.append(summ[1])
        xgraphpos.append(summ[2])
        #return summ
