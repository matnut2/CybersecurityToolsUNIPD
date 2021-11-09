# This program is used to convert ZERO and ONE to 0 and 1. This version can also consider the space character.
# After the elaboration, the output will be sent to 'binary.txt'

f = open('zero_one', 'r')          # Insert here input file
string = f.read()
f.close()

i = 0


with open('binary.txt', 'w') as o:      # Create a new file called 'binary.txt' to write the output
    while i < len(string):
        if string[i:i+4] == 'ZERO':
            o.write('0')
            i += 4
            print('found zero')
        elif string[i:i+3] == 'ONE':
            o.write('1')
            i += 3
            print('found one')

        elif string[i] == ' ' or string[i] == '\n':
            i += 1
            print('white space')
