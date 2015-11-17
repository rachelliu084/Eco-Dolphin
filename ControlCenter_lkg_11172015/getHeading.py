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
