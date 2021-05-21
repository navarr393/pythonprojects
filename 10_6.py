
try:
    
    x=input("Number 1: ")
    x=int(x)
    y=input("Number 2: ")
    y=int(y)
    
except ValueError:
    
    print("A non interger was entered!")
    
else:
    
    s=x+y
    print(f"The sum of both numbers is {s}!")