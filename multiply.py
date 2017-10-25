#Matthew Siegel
#10/25/17
#multiply.py - multiplying game

from random import randint
counter = 0
while True:
    num1 = randint(1,10)
    num2 = randint(1,10)
    if int(input('What is',num1,'*',num2,'? ')) == num1*num2:
        counter+=1
    if counter == 5:
        statement()
    
def statement():
    randnum = drandint(1,5)
    if randnum == 1:
        print('You got this keep going')
    elif randnum == 2:
        print('You are doing better than Gary!')
    elif randnum == 3:
        print('You are doing better than Eric!')
    elif randnum == 4:
        print('NAILED IT')
    elif randnum == 5:
        print('Keep going!')
    
    
