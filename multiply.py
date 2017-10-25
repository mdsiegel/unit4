#Matthew Siegel
#10/25/17
#multiply.py - multiplying game

from random import randint
counter = 0
while true:
    num1 = randint(1,10)
    num2 = randint(1,10)
    if int(input('What is',num1,'*',num2,'? ')) == num1*num2:
        counter+=1
    

