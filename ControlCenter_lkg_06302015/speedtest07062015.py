import serial
import math
import time
import plotly.plotly as py
from plotly.graph_objs import *
from array import *

# Global variables defined as follows
fob = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/accel.txt','w')
fob2 = open('/home/pi/Eco-Dolphin1/ControlCenter_lkg_06112015/ylocation.txt','w')
port = '/dev/ttyACM0'
baud = 57600
response = ''

#commands to agent
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


#tracking variables
bounds = [20.0,20.0,10.0]
bed = [0.0,0.0,0.0]
targetangle = [0.0,0.0,0.0]
angle = [0.0,0.0,0.0]
heading = [0.0,0.0,0.0]
acceleration = [0.0,0.0,0.0]
destination = [12.0,12.0,5.0]
location = [0.0,0.0,0.0]
prevlocation = [0.0,0.0,0.0]
prevaccel=[0.0,0.0,0.0]
prevangle = [0.0,0.0,0.0]
prevtime = time.clock()
Gyro = '7'
tolerance = 2.0
elapsetime = 0.0
summ = [0,0,0]
diff = [0,0,0]
diffaccel = [0.0,0.0,0.0]
diffgyro = [0.0,0.0,0.0]
xgraphpos = list()
ygraphpos = list()
zgraphpos = list()





#Cp = measure battery

#loop counters

i = 0 #for file population (maximum: 100)
n = 0 #for IMU calibration (average acceleration)

#Serial communication definition and initialization
ser = serial.Serial(port, baud, timeout=1)
ser.open()

#function definitions - hover, setBoundary, getPosition,  setBoundary, setAcceleration, resurface
def isfloat(value):
        try:
                float(value)
                return True
        except ValueError:
                return False

def cmdAgent(command):
      global response
      ser.write(command)
      response  = ser.readline()
      print response
      return  response

def separateString(string):
    global response

    beginx = response.find('=')+1
    endx = response.find(',')
    imux = response[beginx:endx]
    beginy = endx+1
    endy = response[beginy::].find(',')+beginy
    imuy = response[beginy:endy]
    beginz = endy+1
    endz = response[beginz::].find('r')-1
    imuz = response[beginz:endz]
    values = [imux, imuy, imuz]
    return values



def getPosGraph(xgraphpos,ygraphpos,zgraphpos,p):
  s = str(p)
  trace2 = Scatter3d(
       x = xgraphpos,
       y = ygraphpos,
       z = zgraphpos,
        mode='lines',
        marker=Marker(
            color='#1f77b4',
            size=12,
            symbol='circle',
            line=Line(
                color='rgb(0,0,0)',
                width=0
            )
        ),
        line=Line(
            color='rgb(50,0,0)',
            width=1
        )
    )
  
    data = Data([trace1])
    layout = Layout( 
              autosize=False,
              width=500,
              height=500,
              margin=Margin(
              l=0,
              r=0,
              b=0,
              t=65
            )
        )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Eco-Dolphin1Graph3DPosition ' + p)

def getPosition():
    global acceleration
    global location
    global prevaccel
    global diffaccel
    global response
    global prevlocation
    global summ
    global xgraphaccel
    global ygraphaccel
    global zgraphaccel
    global xgraphpos
    global ygraphpos
    global zgraphpos

    #get the acceleration and separate string
    cmdAgent(PwrOn)
    response = cmdAgent(Accel)
    print response
    accelstring = separateString(response)
    if isfloat(accelstring[0]) and isfloat(accelstring[1]) and isfloat(accelstring[2]):
    #convert and assign acceleration values

        accelx = float(accelstring[0])
        accely = float(accelstring[1])
        accelz = float(accelstring[2])
        acceleration = [accelx,accely,accelz]
        


    #record the acceleration in a file
        fob.write('Accel: ')
        fob.write('%03d, ' % acceleration[0])
        fob.write('%03d, ' % acceleration[1])
        fob.write('%03d\n' % acceleration[2])

    #calculate the change in acceleration
        diffaccel[0] = acceleration[0] - prevaccel[0]
        diffaccel[1] = acceleration[1] - prevaccel[1]
        diffaccel[2] = acceleration[2] - prevaccel[2]
        magaccel = math.sqrt((math.pow(diffaccel[0],2))+(math.pow(diffaccel[1],2))+(math.pow(diffaccel[2],2)))
        
        #After computin the accel, the list will add the following acceleration 
        

        
  

    #assign previous acceleration to the current acceleration
        prevaccel = acceleration

    #establish current location
        location[0] = 0.5*diffaccel[0]*math.pow(difftime,2)
        location[1] = 0.5*diffaccel[1]*math.pow(difftime,2)
        location[2] = 0.5*diffaccel[2]*math.pow(difftime,2)
    #the vector summ shows the position
        summ[0] += location[0] + prevlocation[0]
        summ[1] += location[1] + prevlocation[1]
        summ[2] += location[2] + prevlocation[2]
        print summ

    #assign previous location to current location
        prevlocation = location


    #publish location and elapsed time to file server
        fob2.write('Place/Time: ')
        fob2.write('%03d, ' % summ[0])
        fob2.write('%03d, ' % summ[1])
        fob2.write('%03d, ' % summ[2])
        fob2.write('%03d\n' % elapsetime)

        #Add the following position to each list 
        xgraphpos.append(summ[0])
        ygraphpos.append(summ[1])
        xgraphpos.append(summ[2])
        
        return summ

def getHeading():
    global diffgyro
    global heading
    global Gyro

        #get heading information from the agent
    response = cmdAgent(Gyro)
    gyrostring = separateString(response)
    print gyrostring
    if isfloat(gyrostring[0]) and isfloat(gyrostring[1]) and isfloat(gyrostring[2]):
       gyrox = float(gyrostring[0])
       gyroy = float(gyrostring[1])
       gyroz = float(gyrostring[2])
       heading = [gyrox, gyroy, gyroz]


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

    elif(bounds[0] > location[0]): #If the value of the x-coordinate given is less than the target x-coordinate then the machine will move right
        response = cmdAgent(Right)


    if(bounds[1] < location[1]):
        response = cmdAgent(Back) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move backward

    elif(bounds[1] > location[1]):
        response = cmdAgent(Fwd) #If the value of the y-coordinate given is greater than the target y-coordinate then the machine will move forward


    if(bounds[2] < location[2]):
        response = cmdAgent(Dive)

    elif(bounds[2] > location[2]):
        response = cmdAgent(Rise)


    if(bounds[0]==location[0])and(bounds[1]==location[1])and(bounds[2]==location[2]):
        response = cmdAgent(Idle)
        #Theoretically, the machine will go "IDLE" or cease of all movement should the machine reach its targetted coordinates.
        print 'Target destination reached'
    return response

def resurface():
    global tolerance
    global location

    while location[2] > tolerance:
       cmdAgent(Rise)
       getPosition()
       return 0

def proximity ():
    global location
    global bed
    r = math.sqrt((math.pow((n[0]-coor[0]),2))+(math.pow((n[1]-coor[1]),2))+(math.pow((n[2]-coor[2]),2)))
    if(r < tolerance):
      avoid()

def avoid():
    global coor
    global n
    if(coor[2] < n[2]):
      ser.write(Dive)
    else:
      ser.write(Rise)

def tolI():
    global currentx
    global currenty
    global currentz
    #getCurrent()
        #goaldistance = math.sqrt((math.pow((destinationx-currentx),2))+(math.pow((destinationy-currenty),2))+(math.pow((destinationz-currentz),2)))
        #goaltime = (current speed)/goaldistance
        #Itime = (Cp/math.pow(get.Current(),1.333))
        #tolIt = Itime- goaltime

#def chkabort():
        #getCurrent()
        #tolI()
        #print getCurrent()
        #if
           #tolIt < 0
           #resurface()
           #set destination[0,0,0]
           #print 'abort'
        #else
           #continue

#def chkoverride():
        #ser.readline()
        #if
           #ser.readline() = 'override'
           #resurface()
           #set destination[0,0,0]
           #print 'override'
        #else
           #continue

#main code begins here
setBoundary(bounds[0],bounds[1],bounds[2])
response = cmdAgent(PwrOn)
print response
difftime = time.clock() + prevtime
#stringtime = str(difftime)
#local variables
endx = 0
beginy = 0
endy = 0
beginz = 0
endz = 0
#functional loop
while i < 6:
   elapsetime+=time.clock()
   #check if destination has been reached
   if (location == destination) or (location > bounds):
        while difftime < 15:
           ser.write(Hover)
           difftime+=time.clock()
        #write to sonar
                #retreat
           resurface()
           response  = cmdAgent(PwrOff)
   else:
                #check the state of the agent
        if response == "" or response == 'Ready':
           getPosition()

           cmdAgent(Fwd)
           time.sleep(1)
           cmdAgent(Back)
           time.sleep(1)
           cmdAgent(Right)
           time.sleep(1)
           cmdAgent(Fwd)
           time.sleep(1)
           cmdAgent(Left)
           time.sleep(1)
           cmdAgent(Fwd)
           time.sleep(1)
           cmdAgent(Dive)
           time.sleep(1)
           cmdAgent(Rise)
           time.sleep(1)
           cmdAgent(Left)
           time.sleep(1)
           cmdAgent(Fwd)
           time.sleep(1)
           cmd.Agent(Left)
           time.sleep(1)
           cmd.Agent(Fwd)
           time.sleep(1)

           cmdAgent(PwrOff)
           #cmdAgent(PwrOn)
           #print summ
           #getHeading()

           #calculate the change in position
           diff[0] = location[0] - prevlocation[0]
           diff[1] = location[1] - prevlocation[1]
           diff[2] = location[2] - prevlocation[2]
           maglocation = math.sqrt((math.pow(diff[0],2))+(math.pow(diff[1],2))+(math.pow(diff[2],2)))

           #reassign previous location to current location
           #prevlocation=location
           n+=1
          # if n>15:#average the acceleration
            #checkPoint()
#            toHeading()
        else:#add Ready, Abort, Override option
                print 'Not Ready'
                response = cmdAgent(PwrOn)
   if(i == 100):
       p = i / 100
       getPosGraph(xgraphpos,ygraphpos,zgraphpos, p)


   i+=1
#When the loop ends,the functions 'getGraphAccel' and 'getPosGraph' will then take in the array lists 
#from the other functions and then creat a graph from these data.    
