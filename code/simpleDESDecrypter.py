# Funzioni per la trasformazione tra testo e binario
def string2binary(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def binary2string(text):
    return ''.join(f'{ord(c):08b}' for c in text)

# Funzione che divide un blocco in due blocchi da 6 bit
def splitblock(block):
    Lr = block[:6]
    Rr = block[6:]
    return Lr, Rr

# Funzione che serve per espandere un blocco come descritto
def expand_miniblock(b):
    return b[0] + b[1] + b[3] + b[2] + b[3] + b[2] + b[4] + b[5]

# XOR 
def xor(a, b):
    res = int(a, 2) ^ int(b, 2)
    return f'{res:08b}'

# Regole 9 applicate per S1 e S2
def rule9S1(a):
    row = int(a[0])
    col = int(a[1:], 2)

    matrix = [['101','010', '001', '110', '011', '100', '111', '000'],
        ['001',	'100',	'110',	'010',	'000','111',	'101',	'011']
    ]

    return matrix[row][col]

def rule9S2(a):
    row = int(a[0])
    col = int(a[1:], 2)

    matrix = [['100','000','110','101','111','001','011','010'],
        ['101','011','000','111','110','010','001','100']]

    return matrix[row][col]

# Encryption Function
def encrypt(text, key, R):
    text_encr = ''

    text_bin = string2binary(text)
    if (len(text_bin) % 12 ) != 0:
        raise Exception('Error in rule 1')

    key_bin = string2binary(key)
    if (len(key_bin) < 8):
        raise Exception('Error in rule 2')

    for bnum in range(len(text_bin) // 12):
        i = bnum

        from_   = 0 + 12*bnum
        to_     = 12*(bnum+1)
        block   = text_bin[from_:to_]

        for r in range(R):
            Lr, Rr = splitblock(block)

            Rr_expanded = expand_miniblock(Rr)
            
            curr_key = key_bin[i * R + r : i * R + r + 8]

            Rr_exp_xor_key = xor(Rr_expanded, curr_key)

            S1 = Rr_exp_xor_key[:4]
            S2 = Rr_exp_xor_key[4:]

            S1update = rule9S1(S1)
            S2update = rule9S2(S2)

            S = S1update + S2update
            if len(S) != 6:
                raise Exception('Error in rule 10')

            newRr = xor(S, Lr)[2:]

            block = Rr + newRr
        text_encr += block
    return text_encr

# Decrypt Function
def decrypt(text, key, R):
    text_bin = text
    key_bin = string2binary(key)
    text_dec = ''

    if len(text_bin) < 8:
        raise Exception('Error in rule 2')

    for bnum in range(len(text_bin) // 12):
        i = bnum

        from_   = 0 + 12*bnum
        to_     = 12*(bnum+1)
        block   = text_bin[from_:to_]

        for r in range(R-1, -1, -1):
            Rr, Rr_alt = splitblock(block)

            Rr_expanded = expand_miniblock(Rr)

            curr_key = key_bin[i * R + r : i * R + r + 8]
            Rr_exp_xor_key = xor(Rr_expanded, curr_key)

            S1 = Rr_exp_xor_key[:4]
            S2 = Rr_exp_xor_key[4:]

            S1update = rule9S1(S1)
            S2update = rule9S2(S2)

            S = S1update + S2update
            if len(S) != 6:
                raise Exception('Error in rule 10')

            Lr = xor(Rr_alt, S)
            Lr = Lr[2:]
            block = Lr + Rr

        new = Lr + Rr
        text_dec += new

    res = ''

    for i in range(len(text_dec) // 8):
        res += chr(int(text_dec[(i*8): ((i+1)*8)], 2))
    print(res)






key = 'mu'
R = 2

en = encrypt('Min0n!', key, R)
decrypt(en, key, R)

