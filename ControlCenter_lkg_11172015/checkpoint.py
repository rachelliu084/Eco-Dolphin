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
