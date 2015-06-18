
import plotly.plotly as py
from plotly.graph_objs import *
from array import *

maxnumber = 20
array1 = array[]
array2 = array[]
for i in range(0,maxnumber):
      array1.append(i)
      array2.append(i+2)




py.sign_in('siamaterau', 'xdttqq9cld')
trace1 = Scatter(
    x=array1,
    y=array2,
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
data = Data([trace1, trace2])
plot_url = py.plot(data)
