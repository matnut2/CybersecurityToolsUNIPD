# This program is used to extract the uppercase characters from an input file
# After the extraction, the result is placed in a file called 'uppercase.txt'

f = open('challenge.txt', 'r')              # Insert here input file
book = f.read()
f.close()

with open('uppercase.txt', 'w') as o:
    for i in book:
        if (i.isupper() == True):
            o.write(i)