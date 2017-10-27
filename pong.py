#Matthew Siegel
#10/27/17
#pong.py

from ggame import *
from random import randint

ROWS = 30
COLLS = 50
CELL_SIZE = 20



if __name__ == '__main__':
    
    data= {}
    data['score'] = 0
    data['frames'] = 0
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    leftBox = RectangleAsset(COLLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    rightBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    ball = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    data['scoreText'] = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(COLLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    Sprite(data['scoreText'],(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().listenKeyEvent('keydown','down arrow', moveDown)



    App().run(step)
