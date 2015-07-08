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
while 1:
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

           #cmdAgent(Fwd)
           #time.sleep(3)

        elif response == 'Interrupt':#add Ready, Abort, Override option
				   #chkoverride()
				
	      else:	
           print 'Not Ready'
           response = cmdAgent(PwrOn)


   i+=1
