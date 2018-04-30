#Matthew Siegel
#4/30/18
#antsDemo.py - using lists with graphics

from ggame import *

ANTS = 10

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(20,LineStyle(1,red),red)
    Sprite(ant)
    
    App().run()
    