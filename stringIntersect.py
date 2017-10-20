#Matthew Siegel
#10/19/17
#stringIntersect.py - Gets a string from the original

def stringIntersect(str1,str2):
    totalStr = ''
    totalStr += str1
        
    totalStr +=str2
    finalStr = ''
    for ch in totalStr:
        if ch in str1 and ch in str2:
            if not ch in finalStr:
                finalStr += ch
        
            
            
    return finalStr
    
print(stringIntersect('mississippi','pennsyvania'))

