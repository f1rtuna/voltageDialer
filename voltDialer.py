import serial
import time
from vpython import *
import numpy as np

# initial arrow to point at voltages
arrowLength = 1
arrowWidth = .02
myArrow = arrow(Length = arrowLength, 
                shaftWidth = arrowWidth, 
                color = color.red, 
                axis = vector(0, 1, 0)
                )

# tick mark parameters along with label params
tickLength = .1
tickWidth = .02
tickHeight = .02

voltage = 0
offset = .3

# generate major tick marks coinciding with voltages 0 - 5
# based on reading from potentiometer on Arduino
for theta in np.linspace(5*np.pi/6, np.pi/6, 6):
    tickMajor = box(color=color.black, 
                    pos=vector(arrowLength * np.cos(theta), 
                               arrowLength * np.sin(theta), 0), 
                    size=vector(tickLength, tickWidth, tickHeight), 
                    axis=vector(arrowLength * np.cos(theta), arrowLength * np.sin(theta), 0)
                    )
    voltLabel = label(text = str(voltage) + ' volts', 
                  box=False, 
                  pos=vector((arrowLength + offset) * np.cos(theta), 
                             (arrowLength + offset) * np.sin(theta), 0)
                  )
    voltage += 1
    
minorTickLength = .05
minorTickWidth = .01
minorTickHeight = .01
for theta in np.linspace(5*np.pi/6, np.pi/6, 51):
    minorTickMajor = box(color=color.black, 
                    pos=vector(arrowLength * np.cos(theta), 
                               arrowLength * np.sin(theta), 0), 
                    size=vector(minorTickLength, minorTickWidth, minorTickHeight), 
                    axis=vector(arrowLength * np.cos(theta), arrowLength * np.sin(theta), 0)
                )

# box to hold arrow and tick marks
boxX = 4
boxY = 2.75
boxZ = .1
myCase = box(color=color.white, size=vector(boxX, boxY, boxZ)/2, pos=vector(0, .95 * boxY/4, -boxZ))

# arduino object to obtain data from serial port
arduinoData = serial.Serial('/dev/cu.usbmodem1201', 9600)
while True:
    # if there is no data just wait
    while(arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    potVal = str(dataPacket, 'utf-8')
    potVal = int(potVal.strip("\r\n"))
    #0 is right np.pi is left
    # theo more voltage the close to left 0
    """ 
    (0, pi/6), (1023, 5pi/6), 
    m = (-2pi / 3069)
    theta = m * potval + 5pi/6
    """
    m = (-2 * np.pi / 3069)
    theta = m * potVal + 5 * np.pi / 6
    myArrow.axis = vector(arrowLength * np.cos(theta), arrowLength * np.sin(theta), 0)