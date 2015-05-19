import serial
import math
import time

port = '/dev/ttyACM2'
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
set = 'IMUSet'
ready = 'Ready'
targetmag = 89
targetx = 20
targety = 20
targetz = 20
tol = 3
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

ser = serial.Serial(port, baud, timeout=1)
ser.open()

def hover(x, y, z):
    targettime = time.clock()+10
    while(time.clock() < targettime):
         if(y < 0):
            ser.write(forward)

         elif(y > 0):
            ser.write(backward)
         else:
           ser.write(idle)


         if(x < 0):
            ser.write(right)
         elif(x > 0):
           ser.write(left)
         else:
           ser.write(idle)

         if(z < 0):
           ser.write(rise)
         elif(z > 0):
           ser.write(dive)
         else:
           ser.write(idle)
         
def resurface (z)

        while z>tol
        
           serial.write(rise)
           #get z to see if at surface yet
           
def getcoordinate():
     coor = []
     coor.append(xaccel)
     coor.append(yaccel)ser.write(pwr)
        print 'testing1'
        while 1:
           print 'testing2'
           responsepwr = ser.readline()
           print responsepwr
    
#Get IMU data once the initialization is complete
           if (responsepwr == 'Ready'):
             responsex = getIMU(x,move)
             responsey = getIMU(y,move)
             responsez = getIMU(z,move)
             responsegyrox = getIMU(gyrox,move)
             responsegyroy = getIMU(gyroy,move)
             responsegyroz = getIMU(gyroz,set)
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
# Convert the string input to floating point decimal and print
             xaccel = float(responsex)
             yaccel = float(responsey)
             zaccel = float(responsez)
             print 'Accel x: ', xaccel
             print 'Accel y: ', yaccel
             print 'Accel z: ', zaccel
             anglex = float(responsegyrox)
             angley = float(responsegyroy)
             anglez = float(responsegyroz)
             print 'Angle x: ', anglex
             print 'Angle y: ', angley
	     print 'Angle z: ', anglez

# Find the difference in the coordinates against the previous values
             diffx = xaccel - prevx
             diffy = yaccel - prevy
             diffz = zaccel - prevz
             difftime = time.clock() - prevtime
             deltax = 0.5*diffx*math.pow(difftime,2)
             deltay = 0.5*diffy*math.pow(difftime,2)
             deltaz = 0.5*diffz*math.pow(difftime,2)

# figure out current location based on acceleration and time
             currentx = deltax + prevdeltax
             currenty = deltay + prevdeltay
             currentz = deltaz + prevdeltaz
             diffanglex = anglex - preanglex
             diffangley = angley - preangley
             diffanglez = anglez - preanglez

# find change in angle, acceleration, and distance in x,y,z
             diffaccel = math.sqrt((math.pow(diffx,2))+(math.pow(diffy,2))+(math.pow(diffz,2)))
             diffangle = math.sqrt((math.pow(diffanglex,2))+(math.pow(diffangley,2))+(math.pow(diffanglez,2)))

# reassign the previous to the current
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
# figure out the next manuever and send thruster command
             responsethr = ser.readline()
             if (responsethr == 'Th_Set'):
		currentangle = math.cos(anglex/angley)
		if(targetmag < currentangle):
             	   ser.write(left)
                elif(targetmag > currentangle):
                   ser.write(right)
		else:
            	   ser.write(idle)
# check position against target position (within tolerance)
             if(((xaccel > targetx + tol)or(xaccel < targetx - tol))and 
		((yaccel > targety + tol)or(yaccel < targety - tol))and 
		((zaccel > targetz + tol)or(zaccel < targetz - tol))):
               continue
             else:
                hover(xaccel, yaccel, zaccel)

# print output
             print 'Change in acceleration: ', diffaccel
             print 'x = ', currentx
             print 'y = ', currenty
             print 'z = ', currentz
             print 'time elapsed: ', difftime
             print 'code success'
          
   except KeyboardInterrupt:
             ser.close()

             coor.append(zaccel)
             ser.write(pwr)
             print 'testing1'
             while 1:
             print 'testing2'
             responsepwr = ser.readline()
             print responsepwr
    
#Get IMU data once the initialization is complete
           if (responsepwr == 'Ready'):
             responsex = getIMU(x,move)
             responsey = getIMU(y,move)
             responsez = getIMU(z,move)
             responsegyrox = getIMU(gyrox,move)
             responsegyroy = getIMU(gyroy,move)
             responsegyroz = getIMU(gyroz,set)
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
# Convert the string input to floating point decimal and print
             xaccel = float(responsex)
             yaccel = float(responsey)
             zaccel = float(responsez)
             print 'Accel x: ', xaccel
             print 'Accel y: ', yaccel
             print 'Accel z: ', zaccel
             anglex = float(responsegyrox)
             angley = float(responsegyroy)
             anglez = float(responsegyroz)
             print 'Angle x: ', anglex
             print 'Angle y: ', angley
	     print 'Angle z: ', anglez

# Find the difference in the coordinates against the previous values
             diffx = xaccel - prevx
             diffy = yaccel - prevy
             diffz = zaccel - prevz
             difftime = time.clock() - prevtime
             deltax = 0.5*diffx*math.pow(difftime,2)
             deltay = 0.5*diffy*math.pow(difftime,2)
             deltaz = 0.5*diffz*math.pow(difftime,2)

# figure out current location based on acceleration and time
             currentx = deltax + prevdeltax
             currenty = deltay + prevdeltay
             currentz = deltaz + prevdeltaz
             diffanglex = anglex - preanglex
             diffangley = angley - preangley
             diffanglez = anglez - preanglez

# find change in angle, acceleration, and distance in x,y,z
             diffaccel = math.sqrt((math.pow(diffx,2))+(math.pow(diffy,2))+(math.pow(diffz,2)))
             diffangle = math.sqrt((math.pow(diffanglex,2))+(math.pow(diffangley,2))+(math.pow(diffanglez,2)))

# reassign the previous to the current
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
# figure out the next manuever and send thruster command
             responsethr = ser.readline()
             if (responsethr == 'Th_Set'):
		currentangle = math.cos(anglex/angley)
		if(targetmag < currentangle):
             	   ser.write(left)
                elif(targetmag > currentangle):
                   ser.write(right)
		else:
            	   ser.write(idle)
# check position against target position (within tolerance)
             if(((xaccel > targetx + tol)or(xaccel < targetx - tol))and 
		((yaccel > targety + tol)or(yaccel < targety - tol))and 
		((zaccel > targetz + tol)or(zaccel < targetz - tol))):
               continue
             else:
                hover(xaccel, yaccel, zaccel)

# print output
             print 'Change in acceleration: ', diffaccel
             print 'x = ', currentx
             print 'y = ', currenty
             print 'z = ', currentz
             print 'time elapsed: ', difftime
             print 'code success'
          
except KeyboardInterrupt:
        ser.close()
     return coor

def getIMU(command,setting):
      #get the response by  sending a request from the agent
      ser.write(command)
      responsecmd = ser.readline()

      #prepare for the next request by setting the mode
      ser.write(setting)
      responseready = ser.readline()

      return  responsecmd

try:
        ser.write(pwr)
        print 'testing1'
        while 1:
           print 'testing2'
           responsepwr = ser.readline()
           print responsepwr
    
#Get IMU data once the initialization is complete
           if (responsepwr == 'Ready'):
             responsex = getIMU(x,move)
             responsey = getIMU(y,move)
             responsez = getIMU(z,move)
             responsegyrox = getIMU(gyrox,move)
             responsegyroy = getIMU(gyroy,move)
             responsegyroz = getIMU(gyroz,set)
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
# Convert the string input to floating point decimal and print
             xaccel = float(responsex)
             yaccel = float(responsey)
             zaccel = float(responsez)
             print 'Accel x: ', xaccel
             print 'Accel y: ', yaccel
             print 'Accel z: ', zaccel
             anglex = float(responsegyrox)
             angley = float(responsegyroy)
             anglez = float(responsegyroz)
             print 'Angle x: ', anglex
             print 'Angle y: ', angley
	     print 'Angle z: ', anglez

# Find the difference in the coordinates against the previous values
             diffx = xaccel - prevx
             diffy = yaccel - prevy
             diffz = zaccel - prevz
             difftime = time.clock() - prevtime
             deltax = 0.5*diffx*math.pow(difftime,2)
             deltay = 0.5*diffy*math.pow(difftime,2)
             deltaz = 0.5*diffz*math.pow(difftime,2)

# figure out current location based on acceleration and time
             currentx = deltax + prevdeltax
             currenty = deltay + prevdeltay
             currentz = deltaz + prevdeltaz
             diffanglex = anglex - preanglex
             diffangley = angley - preangley
             diffanglez = anglez - preanglez

# find change in angle, acceleration, and distance in x,y,z
             diffaccel = math.sqrt((math.pow(diffx,2))+(math.pow(diffy,2))+(math.pow(diffz,2)))
             diffangle = math.sqrt((math.pow(diffanglex,2))+(math.pow(diffangley,2))+(math.pow(diffanglez,2)))

# reassign the previous to the current
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
# figure out the next manuever and send thruster command
             responsethr = ser.readline()
             if (responsethr == 'Th_Set'):
		currentangle = math.cos(anglex/angley)
		if(targetmag < currentangle):
             	   ser.write(left)
                elif(targetmag > currentangle):
                   ser.write(right)
		else:
            	   ser.write(idle)
# check position against target position (within tolerance)
             if(((xaccel > targetx + tol)or(xaccel < targetx - tol))and 
		((yaccel > targety + tol)or(yaccel < targety - tol))and 
		((zaccel > targetz + tol)or(zaccel < targetz - tol))):
               continue
             else:
                hover(xaccel, yaccel, zaccel)

# print output
             print 'Change in acceleration: ', diffaccel
             print 'x = ', currentx
             print 'y = ', currenty
             print 'z = ', currentz
             print 'time elapsed: ', difftime
             print 'code success'
          
except KeyboardInterrupt:
        ser.close()
