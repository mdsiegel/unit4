#Matthew Siegel
#10/25/17
#sunrise.py - making a sunrise

def step():
    ball.y +=3

if __name__ == '__main__':
    yellow = Color(0xFDB813,1)
    yellowOutline = LineStyle(1,yellow) #pixels,color
    
    circle = CircleAsset(50, yellowOutline, yellow)
    ball = Sprite(circle,(20,20))
    
    data = {}
    data['directionx'] = 20
    data['directiony'] = 20
    
    App().run(step)
