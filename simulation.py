from vpython import *
from time import *
import numpy as np


wallThickness=.1
floorWidth=40
floorLengeth=20
roomHeight=40

#floorModel
flooredge1=box(pos=vector(0,-roomHeight/2,-(floorLengeth/2)),size=vector(floorWidth,wallThickness,0.5), color=color.green)
flooredge2=box(pos=vector(0,roomHeight/2,-(floorLengeth/2)),size=vector(floorWidth,wallThickness,0.5), color=color.green)
floor=box(pos=vector(0,0,-floorLengeth/2),size=vector(floorWidth,roomHeight,wallThickness), color=color.white)
flooredge=box(pos=vector(0,0,(-floorLengeth/2)-0.1),size=vector(floorWidth+1,roomHeight+1,wallThickness), color=color.blue)
flooredge3=box(pos=vector(-floorWidth/2,0,-(floorLengeth/2)),size=vector(wallThickness,roomHeight,0.5), color=color.green)
flooredge4=box(pos=vector(floorWidth/2,0,-(floorLengeth/2)),size=vector(wallThickness,roomHeight,0.5), color=color.green)

#vehicleModel
truckbody = box(pos=vector(0,0,0),size=vector(1,2,1),color=color.red)
truckhead = box(pos=vector(0,1.5,0.23),size=vector(1,1,-1.45),color=color.cyan)
truck1 = compound([truckbody, truckhead])
truck2 = compound([truckbody, truckhead])
truck3 = compound([truckbody, truckhead])

carbody2 = box(pos=vector(0,0,0),size=vector(2,1,1),color=color.magenta)
carhead2 = box(pos=vector(-1.5,0,0.23),size=vector(1,1,-1.45),color=color.purple)
car = compound([carbody2, carhead2])

runcar =0
def runCarRadio(x):
    global runcar
    if x.checked==True:
        runcar=1
    if x.checked==False:
        runcar=0
radio(bind=runCarRadio,text='Run Car')

def findDistTruck3andCar():
    carPosition = (car.pos.x, car.pos.y,car.pos.z)
    truck3Postion = (truck3.pos.x, truck3.pos.y,truck3.pos.z) 
    carPos = np.array(carPosition)
    truckPos = np.array(truck3Postion)
    dist = np.linalg.norm(truckPos-carPos)
    return dist 

def findDistTruck2andCar():
    carPosition = (car.pos.x, car.pos.y,car.pos.z)
    truck2Postion = (truck2.pos.x, truck2.pos.y,truck2.pos.z) 
    carPos = np.array(carPosition)
    truckPos = np.array(truck2Postion)
    dist = np.linalg.norm(truckPos-carPos)
    return dist

def findDistTruck1andCar():
    carPosition = (car.pos.x, car.pos.y,car.pos.z)
    truck1Postion = (truck1.pos.x, truck1.pos.y,truck1.pos.z) 
    carPos = np.array(carPosition)
    truckPos = np.array(truck1Postion)
    dist = np.linalg.norm(truckPos-carPos)
    return dist

deltaX=.15
xPos=0
deltaY=.3
yPos=0
distTrcuk1and2 = 5
distTrcuk2and3 = 5
runTruck1 = 0
truckAcceleration= 0



while True:
    rate(25)
    xPos=xPos+deltaX*runTruck1
    yPos=yPos+deltaY*runcar
    
    distTruck3andCar = findDistTruck3andCar()
    distTruck2andCar = findDistTruck2andCar()
    distTruck1andCar = findDistTruck2andCar()    

    #runVehicle
    if (xPos>((floorWidth/2)-11.5) or xPos<((-floorWidth/2)+1.5)):
        deltaX=deltaX*(-1)
    truck1.pos=vector(-(floorWidth/2)+1,xPos,-9)
    truck2.pos = truck1.pos + vector(0,distTrcuk1and2,0)
    truck3.pos = truck2.pos + vector(0,distTrcuk2and3,0)

    if (yPos>((floorWidth/2)-1.5) or yPos<((-floorWidth/2)+20)):
        deltaY=deltaY*(-1)
    car.pos=vector(-yPos,0,-9)
    
    if (distTruck3andCar>5 and distTruck2andCar>7 and distTruck1andCar>10):
        runTruck1 = 1
    else:
        runTruck1 = 0
    
    