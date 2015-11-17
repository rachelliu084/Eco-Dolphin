import serial
port = '/dev/ttyACM0'
baud = 57600

ser = serial.Serial(port, baud, timeout=1)
ser.open()
def cmdAgent(command):
      global response
      ser.write(command)
      response  = ser.readline()
      print response
      return  response
