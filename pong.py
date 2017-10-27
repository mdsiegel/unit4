#Matthew Siegel
#10/27/17
#pong.py


from ggame import *
from random import randint


def moveUp(event):
    rightBoxS.y -=50
def moveDown(event):
    rightBoxS.y += 50
def moveUpL(event):
    leftBoxS.y -=50
def moveDownL(event):
    leftBoxS.y += 50
def step():
    if ball.x >= rightBoxS.x and ball.y >= rightBoxS.y and ball.y<=(rightBoxS.y +150):
        data['directionx']*=-1
    elif ball.x <= leftBoxS.x and ball.y >= leftBoxS.y and ball.y<=(leftBoxS.y + 150):
        data['directionx']*=-1
    if ball.y >= 600:
        data['directiony']*=-1
   # if ball.x <= 0:
     #   data['directionx']*=-1
    if ball.y <= 0:
        data['directiony']*=-1
    ball.x+=data['directionx']
    ball.y+=data['directiony']
   

if __name__ == '__main__':
    green = Color(0x00FF00,1)
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black) #pixels,color
    
    circle = CircleAsset(50, blackOutline, green)
    leftBox = RectangleAsset(20,150,LineStyle(1,black),green)
    leftBoxS = Sprite(leftBox)
    rightBox = RectangleAsset(20,150,LineStyle(1,black),green)
    rightBoxS = Sprite(rightBox,(1000,0))
    ball = Sprite(circle,(300,20))
    
    
    data = {}
    data['leftBoxx'] = leftBoxS.x
    data['directionx'] = 7
    data['directiony'] = 7
    
    
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().listenKeyEvent('keydown','down arrow', moveDown)
    App().listenKeyEvent('keydown','w', moveUpL)
    App().listenKeyEvent('keydown','s', moveDownL)

    
    
    App().run(step)