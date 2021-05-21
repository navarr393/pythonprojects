
filenames=["cats.txt","dogs.txt"]

for filename in filenames:
    print(f"reading from file ~ {filename}")
    try:
        with open(filename) as f:
            names=f.read()
    
    except FileNotFoundError:
        print(f"sorry {filename} was not found!")
    
    else:
        print(names)