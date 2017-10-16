#Matthew Siegel
#10/16/17
#colorChangeWindow.py - Makes boxes of colors

from ggame import*
from random import randint

def mouseClick(event):
    randnum = randint(1,4)
    if randnum ==1:
        red = Color(0xff0000, 1)
        line = LineStyle(3,red)
        rectangle = RectangleAsset(100,100,line,red)
    elif randnum ==2:
        yellow = Color(0xffff00, 1)
        line = LineStyle(3,yellow)
        rectangle = RectangleAsset(100,100,line,yellow)
    elif randnum ==3:
        green = Color(0x00ff7f, 1)
        line = LineStyle(3,green)
        rectangle = RectangleAsset(100,100,line,green)
    elif randnum ==4:
        blue = Color(0x0000ff, 1)
        line = LineStyle(3,blue)
        rectangle = RectangleAsset(100,100,line,blue)
    Sprite(rectangle)
    
        


App().listenMouseEvent('click', mouseClick)
App().run()

