
test=True

while test:
    try:   
        """obtains inputs"""
        x=input("Number 1: ")
        x=int(x)
        y=input("Number 2: ")
        y=int(y)
    
    except ValueError:
        """prints message if error was encountered"""
        print("A non interger was entered!")
    
    else:
        """displays sum"""
        s=x+y
        print(f"The sum of both numbers is {s}!")