# This program is used to "encrypt" a string with the caesar chiper

string = ''             # Input string there
output = ''
shift  = 0              # Shift index there

for _ in range(len(string)):
    output += chr(ord(string[_]) + shift)

print(output)