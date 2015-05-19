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
coor = []


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



def getcoordinate():
     coor = []


     coor.append(xcoor)
     coor.append(ycoor)
     coor.append(zcoor)
     return coor

def getIMU(command,setting):
      ser.write(command)
      responsecmd = ser.readline()	 
      
      ser.write(setting)
      responseready = ser.readline()	
      
      return  responsecmd

def getcoordinate():
     try:
        ser.write(pwr)
	#print pwr
        #sleep(10)
        
	print 'testing1'
          # coor =  getcoordinate()
	   print 'testing2'

           responsepwr = ser.readline()

	   print responsepwr
	   print 'testing3'
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
               print responsethr
               ser.write(pwr)
               #responsepwr = ser.readline()
             else:
               print 'testing5'
               print responsethr
	     print responsex
	     print responsey
	     print responsez
             xcoor = float(responsex)
             ycoor = float(responsey)
             zcoor = float(responsez)
             print ('accel x= ', xcoor)
             print ('accel y= ', ycoor)
             print ('accel z= ', zcoor)
	     anglex = float(responsegyrox)
	     angley = float(responsegyroy)
	     anglez = float(responsegyroz)
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



             diffx = xcoor - prevx
             diffy = ycoor - prevy
             diffz = zcoor - prevz
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
	     print 'code sucess'
	     coor.append(currentx)
             coor.append(currenty)
             coor.append(currentz)
             return coor
             
	    # ser.write(move)
     except KeyboardInterrupt:
        ser.close()
        
        #main code
coor = getcoordinate()
