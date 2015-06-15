import serial
import math
import time


# Global variables defined as follows
fob = open('/home/pi/Eco-Dolphin_lkg_06112015/TestSerial/accel.txt','w')
fob2 = open('/home/pi/Eco-Dolphin_lkg_06112015/TestSerial/location.txt','w')
port = '/dev/ttyACM0'
baud = 57600
response = ''

#commands to agent
Accel = '1'
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
<<<<<<< HEAD
Reset = '13'
=======
targetmag = 89
difftime = 0
location = [0,0,0]
destination = [12,12,5]
coor =  [0.0,0.0,0.0]
maxcoor =  [99.0,99.0,99.0]
#Cp = measure battery
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
>>>>>>> origin/master

#tracking variables
bounds = [20.0,20.0,10.0]
targetangle = [0.0,0.0,0.0]
angle = [0.0,0.0,0.0]
acceleration = [0.0,0.0,0.0]
destination = [12.0,12.0,5.0]
prevlocation = [0.0,0.0,0.0]
prevaccel=[0.0,0.0,0.0]
prevangle = [0.0,0.0,0.0]
prevtime = time.clock()
tolerance = 2.0
summ = [0,0,0]
diff = [0,0,0]
diffaccel = 0.0

#loop counters
i = 0 #for file population (maximum: 100)
n = 0 #for IMU calibration (average acceleration)

#Serial communication definition and initialization
ser = serial.Serial(port, baud, timeout=1)
ser.open()

#function definitions - hover, setBoundary, getPosition,  setBoundary, setAcceleration, resurface
def cmdAgent(command):
      ser.write(command)
      responsecmd = ser.readline()
      return  responsecmd 

def separateString(string):
    global response
	
    endx = response.find(',')
    imux = response[5:endx]
    beginy = endx+1
    endy = response[beginy::].find(',')+beginy
    imuy = response[beginy:endy]
    beginz = endy+1
    imuz = response[beginz::]
	values = [imux, imuy, imuz]
	return values

def getPosition()
	global acceleration
	global location
	global prevaccel
	global diffaccel

	#get the acceleration and separate string
    response = cmdAgent(Accel)
    time.sleep(.05)
    accelstring = separateString(response)

    #convert and assign acceleration values
    acceleration = [float(accelstring[0]),float(accelstring[1]),float(accelstring[2])]

    #record the acceleration in a file
    fob.write('Accel: ')
    fob.write('%03d, ' % acceleration[0])
    fob.write('%03d, ' % acceleration[1])
    fob.write('%03d\n' % acceleration[2])

    #calculate the change in acceleration
    diffaccel = acceleration - prevaccel
    magaccel = math.sqrt((math.pow(diffaccel[0],2))+(math.pow(diffaccel[1],2))+(math.pow(diffaccel[2],2)))

    #assign previous acceleration to the current acceleration
    prevaccel = acceleration

    #establish current location
    location = 0.5*diffaccel*math.pow(difftime,2)
	
	#publish location and elapsed time to file server
    fob2.write('Place/Time: ')
    fob2.write('%03d, ' % location[0])
    fob2.write('%03d, ' % location[1])
    fob2.write('%03d, ' % location[2])
    fob2.write('%03d\n' % elapsetime)
	return location

def getHeading()
	#get heading information from the agent
    response = cmdAgent(Gyro)
    gyrostring = separateString(response)
    heading = [float(gyrostring[0]), float(gyrostring[1]), float(gyrostring[2])]
	
    #calculate the current heading
    magheading = math.sqrt((math.pow(diffgyro[0],2))+(math.pow(diffgyro[1],2))+(math.pow(diffgyro[2],2)))
	return heading
	
	
def hover(x, y, z):
	global location
	global tolerance
	currenttime = time.clock()
    targettime = time.clock()+10
    while(currenttime < targettime):
		 currenttime+=time.clock()
         #get current position
		 
         if(y < location[1]+tolerance):
            ser.write(forward)
         elif(y > location[1]+tolerance):
            ser.write(backward)
         else:
           ser.write(idle)
		   
         if(x < location[0]+tolerance):
            ser.write(right)
         elif(x > location[0]+tolerance):
           ser.write(left)
         else:
           ser.write(idle)

         if(z < location[2]+tolerance):
           ser.write(rise)
         elif(z > location[2]+tolerance):
           ser.write(dive)
         else:
           ser.write(idle)
		   
def setBoundary(xcoor,ycoor,zcoor):
    global bounds
    bounds[0] = xcoor
    bounds[1] = ycoor
    bounds[2] = zcoor

def setAcceleration(xcoor,ycoor,zcoor):
	global acceleration
	acceleration[0]=xcoor
	acceleration[1]=ycoor
	acceleration[2]=zcoor
	
def setPoint(point):
	global location
	location[0]=point[0]
	location[1]=point[1]
	location[2]=point[2]

def setTarget(xcoor,ycoor,zcoor):
	global destination
	destination[0]=xcoor
	destination[1]=ycoor
	destination[2]=zcoor
	
def checkPoint():
    global location
    global bounds
    global response
		
    #compare
    if(bounds[0] < location[0]): #If the value of the x-coordinate given is greater than the target x-coordinate then the machine will move left
        response = cmdAgent(Left)
        print 'Current x-coordinate' , location[0]
        print 'Target x-coordinate' , bounds[0]
    elif(bounds[0] > location[0]): #If the value of the x-coordinate given is less than the target x-coordinate then the machine will move right
        response = cmdAgent(Right)
        print 'Current x-coordinate', location[0]
        print 'Target x-coordinate' , bounds[0]

    if(bounds[1] < location[1]):
        response = cmdAgent(Back) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move backward
        print 'Current y-coordinate' , location[1]
        print 'Target y-coordinate' , bounds[1]
    elif(bounds[1] > location[1]):
        response = cmdAgent(Forward) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move forward
        print 'Current y-coordinate' , location[1]
        print 'Target y-coordinate' , bounds[1]

    if(bounds[2] < location[2]):
        response = cmdAgent(Dive)
        print 'Current z-coordinate' , location[2]
        print 'Target z-coordinate' , bounds[2]
    elif(bounds[2] > location[2]):
        response = cmdAgent(Rise)
        print 'Current z-coordinate' , location[2]
        print 'Target z-coordinate' , bounds[2]

    if(bounds[0]==location[0])and(bounds[1]==location[1])and(bounds[2]==location[2]):
        response = cmdAgent(Idle)
        #Theoretically, the machine will go "IDLE" or cease of all movement should the machine reach its targetted coordinates.
        print 'Target destination reached'
    return None

def resurface():
     global tolerance
     global location

<<<<<<< HEAD
     while location[2] > tolerance:
       cmdAgent(Rise)
	   
       
def proximity ():
    global coor
    global n
    r = math.sqrt((math.pow((n[0]-coor[0]),2))+(math.pow((n[1]-coor[1]),2))+(math.pow((n[2]-coor[2]),2)))
       if r < tol
          avoid()
    
def avoid():
    global coor
    global n
          if coor[2] < n[2]
             ser.write(dive)
          else
            ser.write(rise)
=======
def tolC():
	global currentx
        global currenty
        global currentz
        #getCurrent()
	#goald = math.sqrt((math.pow((destinationx-currentx),2))+(math.pow((destinationy-currenty),2))+(math.pow((destinationz-currentz),2)))
	#goaltime = (current speed)/goald
	#Itime = (Cp/math.pow(get.Current(),1.333))
	#tolCt = Itime- goaltime
	
def chkabort():
	#getCurrent()
	#tolC()
	#print getCurrent()
	if
	   #tolCt < 0
	   #resurface()
	   #set destination[0,0,0]
	   #print 'abort'
	else
	   #continue
	   
def chkovride():
	#ser.readline()
	if 
	   #ser.readline = 'override'
	   #resurface()
	   #set destination[0,0,0]
	   #print 'override'
	else
	   #continue
	
	
     while coor[2] > tol:
       coor = getcoordinate()
       ser.write(rise)
>>>>>>> origin/master

#main code begins here
setBoundary(bounds)
response = cmdAgent(PwrOn)
difftime = time.clock() + prevtime
#stringtime = str(difftime)
#local variables
endx = 0
beginy = 0
endy = 0
beginz = 0
endz = 0
#functional loop
while i < 30:
   elapsetime+=time.clock()
   #check if destination has been reached
   if (location == destination) or (location > bounds):
        while difftime < 15:
           ser.write(Hover)
           difftime+=time.clock()
        ser.write(Idle)
        #write to sonar
		#retreat
   else:
<<<<<<< HEAD
		#check the state of the agent
        if (response == '') or (response == 'Ready'):
           getPosition()
           getHeading()
		   		   
           #calculate the change in position
           diff=location-prevlocation
		   maglocation = math.sqrt((math.pow(diff[0],2))+(math.pow(diff[1],2))+(math.pow(diff[2],2)))
		   
           #reassign previous location to current location
           prevlocation=location
		   n+=1
		   if n>15:
				#average the acceleration
        else:#add Ready, Abort, Override option
=======
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
           #chkabort()
           #chkovride()
           ser.write(Left)
           ser.readline()
        else:
>>>>>>> origin/master
                print 'Not Ready'
                response = cmdAgent(PwrOn)


   i+=1
