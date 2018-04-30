#Matthew Siegel
#4/30/18
#warmup14.py - telling the initials of a name

name = input('What is your first and last name: ').split(' ')

i = True
for w in name[0]:
    if i == True:
        firstInitial = w
    i = False

b = True
for ch in name[1]:
    if b == True:
        firstInitial = ch
    b = False
        
print(w,ch)

