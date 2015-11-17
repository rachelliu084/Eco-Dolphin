from array import *
bounds = [20.0,20.0,10.0]

def setBoundary(xcoor,ycoor,zcoor):
    global bounds
    bounds[0] = xcoor
    bounds[1] = ycoor
    bounds[2] = zcoor
    return bounds
    
