import serial
import cmdAgent
import time
from array import *
port = '/dev/ttyACM0'
baud = 57600

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
location = [0.0,0.0,0.0]
tolerance = 2.0
def hover(x, y, z):
    global location
    global tolerance

    currenttime = time.clock()
    targettime = time.clock()+10
    while(currenttime < targettime):
        currenttime+=time.clock()
        #get current position
        if(y < location[1]+tolerance):
          cmdAgent.cmdAgent(Fwd)
        elif(y > location[1]+tolerance):
          cmdAgent.cmdAgent(Back)
        else:
          cmdAgent.cmdAgent(Idle)

        if(x < location[0]+tolerance):
          cmdAgent.cmdAgent(Right)
        elif(x > location[0]+tolerance):
          cmdAgent.cmdAgent(Left)
        else:
          cmdAgent.cmdAgent(Idle)

        if(z < location[2]+tolerance):
          cmdAgent.cmdAgent(Rise)
        elif(z > location[2]+tolerance):
          cmdAgent.cmdAgent(Dive)
        else:
          cmdAgent.cmdAgent(Idle)
