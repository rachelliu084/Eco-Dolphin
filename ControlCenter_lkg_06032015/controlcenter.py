import serial
import math
import time

# Global variables defined as follows
port = '/dev/ttyACM1'
baud = 57600
IMU = 1
PwrOn = 2
PwrOff = 3
Idle = 4
Hover = 5
Motion = 6
Right = 7
Left = 8
Rise = 9
Dive = 10
Fwd = 11
Back = 12
Reset = 13
targetmag = 89
coor = [0.0,0.0,0.0]
maxcoor = [0.0,0.0,0.0]
i = 0
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
            print 'Current x-coordinate' coor[0]
            print 'Target x-coordinate' maxcoor[0]
        elif(maxcoor[0] > coor[0]): #If the value of the x-coordinate given is less than the target x-coordinate then the machine will move right
            ser.write(right)
            print 'Current x-coordinate' coor[0]
            print 'Target x-coordinate' maxcoor[0]

        if(maxcoor[1] < coor[1]):
            ser.write(backward) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move backward
            print 'Current y-coordinate' coor[1])
            print 'Target y-coordinate' maxcoor[1]
        elif(maxcoor[1] > coor[1])):
            ser.write(forward) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move forward
            print 'Current y-coordinate' coor[1])
            print 'Target y-coordinate' maxcoor[1]

        if(maxcoor[2] < coor[2]):
            ser.write(dive)
            print 'Current z-coordinate' coor[2]
            print 'Target z-coordinate' maxcoor[2]
        elif(maxcoor[2] > coor[2]):
            ser.write(rise)
            print 'Current z-coordinate' coor[2]
            print 'Target z-coordinate' maxcoor[2]

        if(maxcoor[0]==coor[0])and(maxcoor[1]==coor[1])and(maxcoor[2]==coor[2]):
            ser.write(idle)
            #Theoretically, the machine will go "IDLE" or cease of all movement should the machine reach its targetted coordinates.
            print 'Target destination reached'


def getIMU(command,setting):
      ser.write(command)
      responsecmd = ser.readline()

      ser.write(setting)
      responseready = ser.readline()

      return  responsecmd


def getcoordinate():
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
     global coor

     try:
        print 'testing1'
        responsepwr = ser.readline()
        print 'Agent: ', responsepwr
        if (responsepwr == 'Ready'):
             responsex = getIMU(x,move)
             responsey = getIMU(y,move)
             responsez = getIMU(z,move)
             responsegyrox = getIMU(gyrox,move)
             responsegyroy = getIMU(gyroy,move)
             responsegyroz = getIMU(gyroz,sett)
             responsethr = ser.readline()
             print responsethr
             if (responsethr == ''):
               print 'testing4'
               ser.write(IMU)
               responseIMU = ser.readline()
               print 'Agent message: ', responseIMU
               ser.write(PwrOn)
               #responsepwr = ser.readline()
             else:
               print 'testing5'
               print responseIMU


             diffx = xaccel - prevx
             diffy = yaccel - prevy
             diffz = zaccel - prevz
             difftime = time.clock() - prevtime
             deltax = 0.5*diffx*math.pow(difftime,2)
             deltay = 0.5*diffy*math.pow(difftime,2)
             deltaz = 0.5*diffz*math.pow(difftime,2)
             currentx = deltax + prevdeltax
             currenty = deltay + prevdeltay
             currentz = deltaz + prevdeltaz
             diffanglex = anglex - preanglex
             diffangley = angley - preangley
             diffanglez = anglez - preanglez

#find change in time, angle, acceleration, and distance in x,y,z
             # difftime = time.clock() - prevtime
             diffaccel = math.sqrt((math.pow(diffx,2))+(math.pow(diffy,2))+(math.pow(diffz,2)))
             diffangle = math.sqrt((math.pow(diffanglex,2))+(math.pow(diffangley,2))+(math.pow(diffanglez,2)))
             #deltax = 0.5*diffx*math.pow(difftime,2)
             #deltay = 0.5*diffy*math.pow(difftime,2)
             # deltaz = 0.5*diffz*math.pow(difftime,2)
#reassign the previous to the current
             prevx = xaccel
             prevy = yaccel
             prevz = zaccel
             prevdeltax = deltax
             prevdeltay = deltay
             prevdeltaz = deltaz
             preanglex = anglex
             preangley = angley
             preanglez = anglez
             prevtime = time.clock()
             #print output
             print 'Change in Accel: ',diffaccel
             print 'Current x: ', currentx
             print 'Current y: ', currenty
             print 'Current z: ', currentz
             print 'Elapsed time: ' difftime
             print 'IMU Settings received: code success'
             coor[0] = currentx
             coor[1] = currenty
             coor[2] = currentz

             return coor

     # ser.write(move)
     except KeyboardInterrupt:
        ser.close()

def resurface
     global tol
     global coor

     while coor 2 > tol
       coor = getcoordinate()
       ser.write(rise)

#main code begins here
ser.write(Reset)
time.sleep(2)
setBoundary(20.0,20.0,10.0)
print coor
ser.write(pwr)
while i<10:

   coor = getcoordinate()
   currentcoor = checkPoint()
   i+=1


# check position against target position (within tolerance)
  if(((coor[0] > targetx + tol)or(coor[0] < targetx - tol))and
              ((coor[1] > targety + tol)or(coor[1] < targety - tol))and
               ((coor[2] > targetz + tol)or(coor[2] < targetz - tol))):
                 continue
  else:
                 hover(coor[0], coor[1], coor[2])
