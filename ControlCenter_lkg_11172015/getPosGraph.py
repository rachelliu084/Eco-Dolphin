
import plotly.plotly as py
from plotly.graph_objs import *
from array import *
def getPosGraph(xgraphpos,ygraphpos,zgraphpos,p):
  s = str(p)
  py.sign_in('siamaterau', 'xdttqq9cld')

  trace1 = Scatter3d(
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
  plot_url = py.plot(fig, filename='Eco-Dolphin1Graph3DPosition ' + s)
