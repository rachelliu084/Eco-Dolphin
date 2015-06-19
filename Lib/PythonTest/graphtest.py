import plotly.plotly as py
from plotly.graph_objs import *
from array import *

maxnumber = 20 #number of elements or spaces avaiable 
array1 = list()  #array1 is created as an empty list since python syntax is weird 
array2 = list()  #another array is created for the sake of the line graph coordinates
for i in range(0,maxnumber): #a for loop is traversed from integer 0 to the maxnumber or in this case 20
      array1.append(i) #within the loop, array1 is being added based on the integer i 
      array2.append(2*i) #array2 is being added based on the integer i multiplied by 2




py.sign_in('siamaterau', 'xdttqq9cld') #"signs in" to our SIAM account
trace1 = Scatter(
    x=array1, #the x-coordinate is based on the values given from the array1
    y=array2, #the y-coordinate is based on the values given from the array2
    name='trace0', 
    xsrc='siamaterau:41:382fcb',
    ysrc='siamaterau:41:382fcb'
)
trace2 = Scatter(
    x=array2, 
    y=array1,
    name='trace1_y',
    xsrc='siamaterau:41:02a6d0',
    ysrc='siamaterau:41:c6995d'
)
data = Data([trace1, trace2]) #data being recorded based on the traces or in other words 'data '
                              # is a variable that takes in both x and y coordinates from trace1 and trace2
plot_url = py.plot(data, filename='arraygraph') #plot_url is a variable that collects the data used in this file and uploads to 
                                                #plotly website based on the given filename
