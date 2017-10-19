#Matthew Siegel
#10/19/17
#mokneyBanana.py - best game ever

from ggame import *
#constants
ROWS = 30
COLLS = 50
CELL_SIZE = 20

def moveRight(event):
    monkey.x +=CELL_SIZE
def moveLeft(event):
    monkey.x -=CELL_SIZE
def moveUP(event):
    monkey.y +=CELL_SIZE
def moveDown(event):
    monkey.y -=CELL_SIZE

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(COLLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    Sprite(bananaBox,(COLLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    
    
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().listenKeyEvent('keydown','down arrow', moveDown)



    App().run()
