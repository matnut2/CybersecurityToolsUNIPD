# This program is used to shift the characters from an input to get the desired string

string  = ''            # Insert here your String
key     = 0             # Insert here your Shift Value
output  = ''            # DON'T TOUCH THIS

for i in range(len(string)):
    output += chr(ord(string[i]) + key)

print(output)
