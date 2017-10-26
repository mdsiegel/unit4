#Matthew Siegel
#10/25/17
#bouncingBall.py - ball bouncing around

from ggame import *
from random import randint

def step():
    if ball.x == 1000:
        data['directionx']*=-1
    if ball.y == 800:
        data['directiony']*=-1
    ball.x+=data['directionx']
    ball.y+=data['directiony']
    print('step')

green = Color(0x00FF00,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #pixels,color

circle = CircleAsset(50, blackOutline, green)
ball = Sprite(circle,(20,20))

data = {}
data['directionx'] = 5
data['directiony'] = 5

App().run(step)

