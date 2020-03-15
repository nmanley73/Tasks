# Program that reads a text file and outputs number of e's

# Count the numbers of charachter e in Moby-Dick.txt file

with open('C:\\Users\\Noel\\Desktop\\moby-Dick.txt', 'rt') as f:
    data = f.read()
    eCount = data.count("e")
    
print("Number of e in text file :", str(eCount))
