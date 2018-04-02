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
    for ch in string:
        return ch
        
print(firstLetter("cool"))

def repeats(x,y,z):
    if x == y :
        return True
    elif y == z:
        return True
    elif z == x :
        return True
    else:
        return False
        
print(repeats("h","h",7))