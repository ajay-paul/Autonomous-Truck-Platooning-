from vpython import *
from time import *

truckbody = box(pos=vector(0,0,0),size=vector(1,2,1),color=color.red)
#truckbody.rotate(angle=90)
truckhead = box(pos=vector(0,1.5,0.23),size=vector(1,1,-1.45),color=color.cyan)
#tyre = cylinder(pos=vector(0.35,0.75,0.25), size=vector(0.25,1,1),radius=0.25, color=color.purple)
truck = compound([truckbody, truckhead])