#Matthew Siegel
#4/2/18
#quiz4.py - Learning how to do a quiz

def count(int):
    for i in range(1,int+1):
        print(i)
        
count(10)

def excitedPrint(string):
    string = string.upper()
    string = string + "!!!"
    print(string)
excitedPrint("hi")

def firstLetter(string):
    i = 1
    for ch in string:
        if i == 1:
            print(ch)
        i+=1
firstLetter("does this work")