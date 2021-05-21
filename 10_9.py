
filenames=["cats.txt","dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as f:
            names=f.read()
    
    except FileNotFoundError:
        pass
    
    else:
        print(f"reading from file ~ {filename}")
        print(names)