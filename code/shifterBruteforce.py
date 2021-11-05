result = dict()
cipher = ''                             # Insert here the input

for shift in range(255):
    flag = ''

    for i in range(len(cipher)):
        if((ord(cipher[i]) + shift) > 255):
            flag += chr(ord(cipher[i]) + shift - 255)
        else:
            flag += chr(ord(cipher[i]) + shift)
    print(flag)
    result[shift] = flag

