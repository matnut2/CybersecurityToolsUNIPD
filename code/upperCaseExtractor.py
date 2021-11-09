# This program is used to extract the uppercase characters from an input file
# After the extraction, the result is placed in a file called 'uppercase.txt'

f = open('inputFile.txt', 'r')              # Insert here input file
book = f.read()
f.close()

with open('uppercase.txt', 'w') as o:       # Create a new file named 'uppercase.txt' to place to write the output
    for i in book:
        if (i.isupper() == True):
            o.write(i)
