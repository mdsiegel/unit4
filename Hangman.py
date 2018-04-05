#Matthew Siegel
#4/4/18
#Hangman.py - hangman game

from ggame import *

black = Color(0x000000,1)

def pickWord():
    return word == "word"

def wordComplete():
    print("You win")
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
    #Spriting all the compoenents of the hangman board
    Sprite(baseLine, (150,400))
    Sprite(vertLine, (300,100))
    Sprite(topLine, (300,100))
    Sprite(hangLine, (400,100))
   
    #Listening for any letter being pressed
    App().listenKeyEvent('keydown','a', keyPress)
    App().listenKeyEvent('keydown','b', keyPress)
    App().listenKeyEvent('keydown','c', keyPress)
    App().listenKeyEvent('keydown','d', keyPress)
    App().listenKeyEvent('keydown','e', keyPress)
    App().listenKeyEvent('keydown','f', keyPress)
    App().listenKeyEvent('keydown','g', keyPress)
    App().listenKeyEvent('keydown','h', keyPress)
    App().listenKeyEvent('keydown','i', keyPress)
    App().listenKeyEvent('keydown','j', keyPress)
    App().listenKeyEvent('keydown','k', keyPress)
    App().listenKeyEvent('keydown','l', keyPress)
    App().listenKeyEvent('keydown','m', keyPress)
    App().listenKeyEvent('keydown','n', keyPress)
    App().listenKeyEvent('keydown','o', keyPress)
    App().listenKeyEvent('keydown','p', keyPress)
    App().listenKeyEvent('keydown','q', keyPress)
    App().listenKeyEvent('keydown','r', keyPress)
    App().listenKeyEvent('keydown','s', keyPress)
    App().listenKeyEvent('keydown','t', keyPress)
    App().listenKeyEvent('keydown','u', keyPress)
    App().listenKeyEvent('keydown','v', keyPress)
    App().listenKeyEvent('keydown','w', keyPress)
    App().listenKeyEvent('keydown','x', keyPress)
    App().listenKeyEvent('keydown','y', keyPress)
    App().listenKeyEvent('keydown','z', keyPress)
    
    

    App().run()
    
    
