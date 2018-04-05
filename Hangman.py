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
    baseLine = LineAsset(100, 100, blackOutline)
    vertLine = LineAsset(50, 160, blackOutline)
    topLine = LineAsset(50, 160, blackOutline)
    hangLine = LineAsset(50, 160, blackOutline)
    
    Sprite(baseLine)
    
    App().run()
    
    
