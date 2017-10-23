#Matthew Siegel
#10/23/17
#trianlge.py - Finding the area of a triangle

def distance(x1,y1,x2,y2):
    distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return distance
print(distance(1,0,20,0))