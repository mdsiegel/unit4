#Matthew Siegel
#3/30/18
#fibonacci.py - Making the fibonacci sequence

def fibonacci(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print(fibonacci(7))
