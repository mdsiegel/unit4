#Matthew Siegel
#10/16/17
#distance.py - Finding the distance between points

def distance(x1,y1,x2,y2):
    distance = ((x2-x1)**2+(y2-y1)**2)**1/2
    print(distance)
distance(3,4,-5,2)