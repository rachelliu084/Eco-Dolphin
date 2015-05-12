import serial
import math
import time

ser = serial.Serial('/dev/ttyACM0',57600, timeout=1)
x = 'Accelx'
y = 'Accely'
z = 'Accelz'
gyrox = 'Gyrox'
gyroy = 'Gyroy'
gyroz = 'Gyroz'
# right = '6'
# left = '7'
# rise = '8'
# dive = '9'
# idle = '10'
# sonarpos = '11'
# forward = '12'
# backward = '13'

targetmag = 89


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

ser.open()

def hover(diffx, diffy, diffz):
    targettime = time.time.clock()
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



def getcoordinate():
     coor = []


     coor.append(xcoor)
     coor.append(ycoor)
     coor.append(zcoor)
     return coor


try:
        ser.wrtie(PowerOn)
        sleep(10)
        while 1:
          # coor =  getcoordinate()
           ser.write(x) 
           responsex = ser.readline()
           ser.write(y)
           responsey = ser.readline()
           ser.write(z)
           responsez = ser.readline()
           ser.write(gyrox)
           anglex = ser.readline()
           ser.write(gyroy)
           angley = ser.readline()
           ser.write(gyroz)
           anglez = ser.readline()
           print responsex
           print responsey
           print responsez
           xcoor = float(responsex)
           ycoor = float(responsey)
           zcoor = float(responsez)
           print xcoor
           print ycoor
           print zcoor
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
              #check(sonar) position
            # if(!waypoint):
              # continue
           # else:
                #hover(targetheading)



           diffx = xcoor - prevx
           diffy = ycoor - prevy
           diffz = zcoor - prevz
           currentx = deltax + prevdeltax
           currenty = deltay + prevdeltay
           currentz = deltaz + prevdeltaz
           diffanglex = anglex - preanglex
           diffangley = angley - preangley
           diffanglez = anglez - preanglez
          

#find change in time, angle, acceleration, and distance in x,y,z
           difftime = time.clock() - prevtime
           diffaccel = math.sqrt((math.pow(diffx,2))+(math.pow(diffy,2))+(math.pow(diffz,2)))
           diffangle = math.sqrt((math.pow(diffanglex,2))+(math.pow(diffangley,2))+(math.pow(diffanglez,2)))
           deltax = 0.5*diffx*math.pow(difftime,2)
           deltay = 0.5*diffy*math.pow(difftime,2)
           deltaz = 0.5*diffz*math.pow(difftime,2)
#reassign the previous to the current
           prevx = xcoor
           prevy = ycoor
           prevz = zcoor
           prevdeltax = deltax
           prevdeltay = deltay
           prevdeltaz = deltaz
           preanglex = anglex
           preangley = angley
           preanglez = anglez
           prevtime = time.clock()
           #print output
           print diffaccel
           print currentx
           print currenty
           print currentz
           print difftime

except KeyboardInterrupt:
        ser.close()
