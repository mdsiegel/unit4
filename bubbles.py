#Matthew Siegel
#10/25/17
#bubbles.py - making bubbles!!!!!

from ggame import *
from random import randint

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels,color
def bubble():
    randnum = randint(1,4)
    if randnum == 1:
        circle = CircleAsset(randint(20,100), blackOutline, red)
    elif randnum == 2:
        circle = CircleAsset(randint(20,100), blackOutline, red)
    elif randnum == 3:
        circle = CircleAsset(randint(20,100), blackOutline, red)
    elif randnum == 4:
        circle = CircleAsset(randint(20,100), blackOutline, red)

    