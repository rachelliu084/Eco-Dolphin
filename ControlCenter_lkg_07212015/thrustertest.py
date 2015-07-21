import serial
import math
import time

# Global variables defined as follows
port = '/dev/ttyACM0'
baud = 57600
pausetime = 3
response = ''
i = 5

# Setup the serial
ser = serial.Serial(port, baud, timeout = 1)
ser.open()

#commands to agent
Accel = '1'
PwrOn = '2'

#main code begins here
ser.write(PwrOn)
response = ser.readline()
print response

#functional loop
while i != 10:
    if response == 'Ready' or response == '':
        ser.write(str(i))
        i += 1
        time.sleep(pausetime)
    else:
        print 'Not Ready'
    time.sleep(1)
    
