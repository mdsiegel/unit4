#Matthew Siegel
#10/19/17
#mokneyBanana.py - best game ever

from ggame import *

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    
    jungleBox = RectangleAsset(800,600,LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()
