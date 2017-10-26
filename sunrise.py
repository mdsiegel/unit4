#Matthew Siegel
#10/25/17
#sunrise.py - making a sunrise

from ggame import *

def step():
    ball.y -=1

yellow = Color(0xFDB813,1)
yellowOutline = LineStyle(1,yellow) #pixels,color
    
circle = CircleAsset(100, yellowOutline, yellow)
ball = Sprite(circle,(500,800))
    

    
App().run(step)
