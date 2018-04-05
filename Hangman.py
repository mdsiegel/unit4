#Matthew Siegel
#4/4/18
#Hangman.py - hangman game

from ggame import *

black = Color(0x000000,1)

def pickWord():
    word == "word"

def wordComplete():
    return True
    
def printHangman():
    print("hangman")
    
    
def keyPress(event):
    print("keypress")
    
if __name__ == '__main__':
    black = Color(0x000000,1)
    blackOutline = LineStyle(4,black) 
    baseLine = LineAsset(300, 0, blackOutline)
    vertLine = LineAsset(0, -300, blackOutline)
    topLine = LineAsset(100, 0, blackOutline)
    hangLine = LineAsset(0, 60, blackOutline)
    
    Sprite(baseLine, (150,400))
    Sprite(vertLine, (300,100))
    Sprite(topLine, (300,100))
    Sprite(hangLine, (400,100))

    App().run()
    
    
