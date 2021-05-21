
filenames=['Are Parents People.txt', 'Seville.txt']
key=input("Enter a word here to and we'll count how often it appears! : ")

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            words=f.read()
    
    except FileNotFoundError:
        print("The file {filename} was not found!")
    
    else:
        print(f"Searching file for '{key}' ~ {filename}")
        wordlist=words.split()
        amount=wordlist.count(key)
        print(f"The word 'the' appears {amount} times!")