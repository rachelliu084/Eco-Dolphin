response = ''

import serial

port = '/dev/ttyACM0'
baud = 57600
ser = serial.Serial(port, baud, timeout=1)
ser.open()


def separateString(response):
    
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
    #print values
    return values
