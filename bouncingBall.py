#Matthew Siegel
#10/25/17
#bouncingBall.py - ball bouncing around

from ggame import *
from random import randint

green = Color(0x00FF00,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels,color
circle = CircleAsset(50, blackOutline, green)
Sprite(circle,(20,20))


def step():
    circle.x+=10
    circle.y+=10
    print('step')

App().run(step)

