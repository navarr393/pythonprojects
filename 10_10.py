
filenames=['Are Parents People.txt', 'Seville.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            words=f.read()
    
    except FileNotFoundError:
        print("The file {filename} was not found!")
    
    else:
        print(f"Searching file for 'the' ~ {filename}")
        wordlist=words.split()
        amount=wordlist.count('the')
        print(f"The word 'the' appears {amount} times!")