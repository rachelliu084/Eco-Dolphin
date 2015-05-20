import serial
import math
import time

# Global variables defined as follows
port = '/dev/ttyACM1'
baud = 57600
x = 'Accelx'
y = 'Accely'
z = 'Accelz'
gyrox = 'Gyrox'
gyroy = 'Gyroy'
gyroz = 'Gyroz'
pwr = 'PowerOn'
pwroff = 'PowerOFF'
move = 'Motion'
right = 'Turn right'
left = 'Turn left'
rise = 'Surface'
dive = 'Descend'
idle = 'Dead zone'
sonarpos = 'Position'
forward = 'Go straight'
backward = 'Go back'
sett = 'IMUSet'
ready = 'Ready'
targetmag = 89
coor = [0,0,0]
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
               ser.write(right)
               responsethr = ser.readline()
               print 'Agent message: ', responsethr
               ser.write(pwr)
               #responsepwr = ser.readline()
             else:
               print 'testing5'
               print responsethr
             #convert the string response to float
             xaccel = float(responsex)
             yaccel = float(responsey)
             zaccel = float(responsez)
             print 'Accel x= ', xaccel
             print 'Accel y= ', yaccel
             print 'Accel z= ', zaccel
             anglex = float(responsegyrox)
             angley = float(responsegyroy)
             anglez = float(responsegyroz)
             print 'Gyro x= ', anglex
             print 'Gyro y= ', angley
             print 'Gyro z= ', anglez
             #ser.write(mag)
             #responsemag = ser.readline()
             #if(targetmag < responsemag):
             #ser.write(left)
             #print float(responsemag)
             #elif(targetmag > responsemag):
              # ser.write(right)
               #print float(responsemag)

             # else:
             # ser.write(idle)
             # ser.write(sonarpos)
             # check(sonar) position
             # if(!waypoint):
             # continue
             # else:
             #hover(targetheading)

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
   
   while z<tol
      getcoordinate()
      ser.write(rise)
      
#main code begins here
ser.write(pwr)
while i<10:

   coor = getcoordinate()
   i+=1
# check position against target position (within tolerance)
  if(((coor[0] > targetx + tol)or(coor[0] < targetx - tol))and
               ((coor[1] > targety + tol)or(coor[1] < targety - tol))and
               ((coor[2] > targetz + tol)or(coor[2] < targetz - tol))):
                  continue
  else:
                 hover(coor[0], coor[1], coor[2])
