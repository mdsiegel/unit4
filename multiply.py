#Matthew Siegel
#10/25/17
#multiply.py - multiplying game

from random import randint
counter = 0
def statement():
    randnum = randint(1,5)
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
    
    
while True:
    num1 = randint(1,10)
    num2 = randint(1,10)
    if int(input('What is'+ str(num1)+'*'+str(num2)+'? ')) == num1*num2:
        counter+=1
    else:
        print('WRONG')
    if counter == 5:
        statement()
