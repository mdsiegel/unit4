#Matthew Siegel
#10/23/17
#trianlge.py - Finding the area of a triangle

x1 = float(input('Enter the x1 value: '))
y1 = float(input('Enter the y1 value: '))
x2 = float(input('Enter the x2 value: '))
y2 = float(input('Enter the y2 value: '))
x3 = float(input('Enter the x3 value: '))
y3 = float(input('Enter the y3 value: '))

def distance(x1,y1,x2,y2):
    distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return distance
a = distance(x1,y1,x2,y2)
b = distance(x2,y2,x3,y3)
c = distance(x1,y1,x3,y3)

s = 0.5*(a+b+c)
print('The area is',(s*(s-a)*(s-b)*(s-c))**1/2)
