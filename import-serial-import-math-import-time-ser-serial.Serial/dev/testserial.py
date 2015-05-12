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
        while 1:
          # coor =  getcoordinate()
           ser.write(x) 
           responsex = ser.readline()
           ser.write(y)
           responsey = ser.readline()
           ser.write(z)
           responsez = ser.readline()
           print float(responsex)
           print float(responsey)
           print float(responsez)
           xcoor = float(responsex)
           ycoor = float(responsey)
           zcoor = float(responsez)
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
          # print coor


           difftime = time.clock() - prevtime
           distance1 = math.sqrt((math.pow(diffx,2))+(math.pow(diffy,2))+(math.pow(diffz,2)))

           prevx = xcoor
           prevy = ycoor
           prevz = zcoor
           prevtime = time.clock()
           print distance1
           print difftime

except KeyboardInterrupt:
        ser.close()
