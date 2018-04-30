#Matthew Siegel
#4/30/18
#warmup14.py - telling the initials of a name

name = input('What is your first and last name: ').split(' ')

i = 0
for w in name[0]:
    if i == 0:
        firstInitial = w
    i = 1

b = True
for ch in name[1]:
    if b == 0:
        secondInitial = ch
    b = 1
        
print(firstInitial,secondInitial)

