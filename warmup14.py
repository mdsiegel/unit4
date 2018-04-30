#Matthew Siegel
#4/30/18
#warmup14.py - telling the initials of a name

name = input('What is your first and last name: ').split(' ')

i = 0
for w in name[0]:
    if i == 0:
        firstInitial = w

b = 0
for ch in name[1]:
    if b == 0:
        firstInitial = ch
        
print(w,ch)

