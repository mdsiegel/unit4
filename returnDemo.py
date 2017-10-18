#Matthew Siegel
#10/18/17
#returnDemo.py - how to use return with a function
from random import randint

def randevevint(low,high):
    num = randint(low,high)
    while num%2 == 1:
        num = randint(low,high)
    return num

r1=randevevint(1,100)
r2=randevevint(1,100)
r3=randevevint(1,100)

print(r1,r2,r3)
    