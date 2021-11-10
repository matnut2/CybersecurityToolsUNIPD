import base64

original_data = "El Psy Congroo"
encrypted_data = "IFhiPhZNYi0KWiUcCls="
encrypted_flag = "I3gDKVh1Lh4EVyMDBFo="

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")


#decode the encryption from base64
enc_data= base64tostring(encrypted_data)
enc_flag= base64tostring(encrypted_flag)

#we know apply the xor to obtain the key
key = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(original_data, enc_data)])

print('key:\t',key)
#this seems a reasonalble key

flag = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(enc_flag, key)])
print("Flag:\t", flag)
#flag: FLAG=Alpacaman