#Matthew Siegel
#4/30/18
#antsDemo.py - using lists with graphics

from ggame import *
from random import randint

ANTS = 100
WIDTH = 600
HEIGHT = 400

def step():
    for ant in data['antList']:
        ant.x += randint(-4,3)
        ant.y += randint(-4,3)

if __name__ == '__main__':
    
    data = {}
    data['antList'] = []
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(20,LineStyle(1,red),red)
    
    
    for i in range(ANTS):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
    