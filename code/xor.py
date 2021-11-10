# This program was created to solve a challenge where the known information were: original data, encrypted data and encrypted flag.
# If your case doesn't include a Base64 encoding, you can just sign row 16 and 17 as comment (# in python for single line comment)

import base64

# Your Input Here
original_data  = ""         
encrypted_data = ""
encrypted_flag = ""

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")


#decode the encryption from base64
enc_data = base64tostring(encrypted_data)
enc_flag = base64tostring(encrypted_flag)

#we know apply the xor to obtain the key
key = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(original_data, enc_data)])

print('key:\t',key)

flag = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(enc_flag, key)])
print("Flag:\t", flag)
