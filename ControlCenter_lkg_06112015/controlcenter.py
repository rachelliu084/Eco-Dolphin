import serial
import math
import time
#from array import array
# Global variables defined as follows
port = '/dev/ttyACM0'
baud = 57600

IMU = '1'
PwrOn = '2'
PwrOff = '3'
Idle = '4'
Hover = '5'
Gyro = '6'
Right = '7'
Left = '8'
Rise = '9'
Dive = '10'
Fwd = '11'
Back = '12'
targetmag = 89
difftime = 0
location = [0,0,0]
destination = [12,12,5]
coor =  [0.0,0.0,0.0]
maxcoor =  [99.0,99.0,99.0]
i = 0
comma = 0
fob = open('/home/pi/Eco-Dolphin_lkg_05262015/TestSerial/out.txt','w')
#matlab = open('/home/pi/Eco-Dolphin/ControlCenter_lkg_06032015/output.m','w')
prevx = 0
prevy = 0
prevz = 0
preanglex = 0
preangley = 0
preanglez = 0
prevdeltax = 0
prevdeltay = 0
prevdeltaz = 0
prevtime = time.clock()

currentx = 0
currenty = 0
currentz = 0

tolex = 0
toley = 0
tolez = 0

avgx = 0
avgy = 0
avgz = 0

diffx = 0
diffy = 0
diffz = 0

accelx = 0
accely = 0
accelz = 0
#Serial communication definition and initialization
ser = serial.Serial(port, baud, timeout=1)
ser.open()

#function definitions - hover, getIMU, getcoordinate, resurface
def hover(diffx, diffy, diffz):
    targettime = time.clock()+10
    while(time.clock() < targettime):
         if(diffy < 0):
            ser.write(forward)

         elif(diffy > 0):
            ser.write(backward)

         else:
           ser.write(idle)


         if(diffx < 0):
            ser.write(right)
         elif(diffx > 0):
           ser.write(left)
         else:
           ser.write(idle)

         if(diffz < 0):
           ser.write(rise)
         elif(diffz > 0):
           ser.write(dive)
         else:
           ser.write(idle)
def setBoundary(xcoor,ycoor,zcoor):
    global coor
    global maxcoor
    maxcoor[0] = xcoor
    maxcoor[1] = ycoor
    maxcoor[2] = zcoor


def checkPoint():

     #DISCLAIMER: THIS CODE WILL MOST LIKELY NOT WORK SO AS OF NOW THIS IS SOME  PESUDOCODING
        global coor
        global maxcoor
        if(maxcoor[0] < coor[0]): #If the value of the x-coordinate given is greater than the target x-coordinate then the machine will move left
            ser.write(left)
            print 'Current x-coordinate' , coor[0]
            print 'Target x-coordinate' , maxcoor[0]
        elif(maxcoor[0] > coor[0]): #If the value of the x-coordinate given is less than the target x-coordinate then the machine will move right
            ser.write(right)
            print 'Current x-coordinate', coor[0]
            print 'Target x-coordinate' , maxcoor[0]

        if(maxcoor[1] < coor[1]):
            ser.write(backward) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move backward
            print 'Current y-coordinate' , coor[1]
            print 'Target y-coordinate' , maxcoor[1]
        elif(maxcoor[1] > coor[1]):
            ser.write(forward) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move forward
            print 'Current y-coordinate' , coor[1]
            print 'Target y-coordinate' , maxcoor[1]

        if(maxcoor[2] < coor[2]):
            ser.write(dive)
            print 'Current z-coordinate' , coor[2]
            print 'Target z-coordinate' , maxcoor[2]
        elif(maxcoor[2] > coor[2]):
            ser.write(rise)
            print 'Current z-coordinate' , coor[2]
            print 'Target z-coordinate' , maxcoor[2]

        if(maxcoor[0]==coor[0])and(maxcoor[1]==coor[1])and(maxcoor[2]==coor[2]):
            ser.write(idle)
            #Theoretically, the machine will go "IDLE" or cease of all movement should the machine reach its targetted coordinates.
            print 'Target destination reached'
        return None

def getIMU(command):
      ser.write(command)
      #ser.readline()
      responsecmd = ser.readline()

      return  responsecmd


def getcoordinate(response):
     global prevx
     global prevy
     global prevz
     global prevdeltax
     global prevdeltay
     global prevdeltaz
     global preanglex
     global preangley
     global preanglez
     global prevtime
     global pointx
     global pointy
     global pointz
     global currentx
     global currenty
     global currentz
     global tolex
     global toley
     global tolez
     global avgx
     global avgy
     global avgz
     global i
     global diffx
     global diffy
     global diffz
     global accelx
     global accely
     global accelz
     global fob
     try:
        print 'testing1'
        fob.write('testing1')
        #responsepwr = ser.readline()
        print 'Agent: ', response
        fob.write(response + '\n')
        if (response == 'Ready'):
             ser.write(IMU)
             responseaccel = ser.readline()
             #ser.write(Gyro)
             responsegyro = ser.readline()
             print 'accel: ', responsegyro
             print 'IMU Settings received: code success'
             return 0 #coor
        else:
             print 'Not Ready'
             fob.write('Not Ready' + '\n')
     # ser.write(move)
     except KeyboardInterrupt:
        ser.close()

def resurface():
     global tol
     global coor

     while coor[2] > tol:
       coor = getcoordinate()
       ser.write(rise)

#main code begins here
setBoundary(20.0,20.0,10.0)
ser.write(PwrOn)
ser.readline()
response = ser.readline()
print response
difftime = time.clock() + prevtime
stringtime = str(difftime)
endx = 0
beginy = 0
endy = 0
beginz = 0
endz = 0
while i < 30:

   
   if location == destination:
        while difftime < 15:
           ser.write(Hover)
        ser.write(Idle)
        #write to sonar
   else:
        if response == '':
                
           accel = getIMU(IMU)
           time.sleep(.05)
           print accel
           endx = accel.find(',')
           imux = accel[5:endx]
	   beginy = endx+1
	   endy = accel[beginy::].find(',')+beginy
           imuy = accel[beginy:endy]
	   beginz = endy+1
           imuz = accel[beginz::]
           ser.write(Left)
           ser.readline()
        else:
                print 'Not Ready'
                response = ser.readline()
     
   
   i+=1
