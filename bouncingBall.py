#Matthew Siegel
#10/25/17
#bouncingBall.py - ball bouncing around

from ggame import *
from random import randint

green = Color(0x00FF00,1)
blackOutline = LineStyle(1,black) #pixels,color
circle = CircleAsset(randint(20,100), blackOutline, green)
Sprite(circle,(20,20))

def step():
    circle.x+=1
    circle.y+=1
App().run()


