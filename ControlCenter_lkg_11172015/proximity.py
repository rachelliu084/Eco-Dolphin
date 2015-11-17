def proximity ():
    global location
    global bed
    r = math.sqrt((math.pow((n[0]-coor[0]),2))+(math.pow((n[1]-coor[1]),2))+(math.pow((n[2]-coor[2]),2)))
    if(r < tolerance):
      avoid()
