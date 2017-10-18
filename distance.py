#Matthew Siegel
#10/16/17
#distance.py - Finding the distance between points

def distance(x1,y1,x2,y2):
    distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return distance
print(distance(1,0,20,0))