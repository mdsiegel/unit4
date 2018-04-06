#Matthew Siegel
#4/4/18
#Hangman.py - hangman game

from ggame import *

black = Color(0x000000,1)
word = "word"
def pickWord():
    print("pick word")

def wordComplete():
    if lettersLeft == 0:
        print("You win")
        return True
    else:
        return False
    
def printHangman():
    print("hangman")
    
    
def keyPress(event):
    print(event.key)
    for ch in word:
        if event.key == ch:
            print("yay")
            for w in range(1,i):
                if data[w] == event.key:
                    print(w)
                    addLetter(event.key, w)
                    
                
                    
            
            
    
if __name__ == '__main__':
    data = {}
    i = 1
    
    for ch in word:
        data[i] = ch
        i += 1
    
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    blackOutline = LineStyle(4,black) 
    baseLine = LineAsset(300, 0, blackOutline)
    vertLine = LineAsset(0, -300, blackOutline)
    topLine = LineAsset(100, 0, blackOutline)
    hangLine = LineAsset(0, 60, blackOutline)
    head = CircleAsset(30, blackOutline, white)
    body = LineAsset(0, -100, blackOutline)
    leftLeg = LineAsset(-60, -70, blackOutline)
    rightLeg = LineAsset(60, -70, blackOutline)
    leftArm = LineAsset(-70, -60, blackOutline)
    rightArm = LineAsset(100, -100, blackOutline)
    
    letterLine = LineAsset(60, 0, blackOutline)
    #Spriting all the compoenents of the hangman board
    Sprite(baseLine, (150,400))
    Sprite(vertLine, (300,100))
    Sprite(topLine, (300,100))  
    Sprite(hangLine, (400,100))
    
    Sprite(head,(370,150))
    Sprite(body,(400,210))
    Sprite(leftLeg,(400,309))
    Sprite(rightLeg,(340,309))
    Sprite(leftArm,(400,250))
    Sprite(leftArm,(400,250))
    

    for x in range(0,i-1):
        Sprite(letterLine, (300 + (x*100),500))
    print(data)
    def addLetter(letter, x):
        text = TextAsset(letter,fill=black,style='bold 40pt Times')
        Sprite(text, (300+((x-.85)*100),450))
    
    
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
    
    
