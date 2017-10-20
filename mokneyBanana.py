#Matthew Siegel
#10/19/17
#mokneyBanana.py - best game ever

from ggame import *
from random import randint
#constants
ROWS = 30
COLLS = 50
CELL_SIZE = 20

#move the monkey right
def moveRight(event):
    if monkey.x < (COLLS-1)*CELL_SIZE:
        monkey.x +=CELL_SIZE
        if monkey.x == banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
#move the monkey left
def moveLeft(event):
    if monkey.x > 0:
        monkey.x -=CELL_SIZE
        if monkey.x == banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
#move the monkey up
def moveUp(event):
    if monkey.y > 0:
        monkey.y -=CELL_SIZE
        if monkey.x == banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()
#move the monkey down
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y +=CELL_SIZE
        if monkey.x == banana.x and monkey.y==banana.y:
            moveBanana()
            updateScore()

#move the banana to random location
def moveBanana():
    banana.x = randint(0,COLLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    data['frames'] = 0
    
#update the score when the monkey gets the banana
def updateScore():
    data['score'] +=1000
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
#checks if it is time to move the banana
def step():
    data['frames'] +=1
    if data['frames'] == 200:
        moveBanana()

#Checks if 
if __name__ == '__main__':
    
    data= {}
    data['score'] = 0
    data['frames'] = 0
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(COLLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    data['scoreText'] = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(COLLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    Sprite(data['scoreText'],(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().listenKeyEvent('keydown','down arrow', moveDown)



    App().run(step)
