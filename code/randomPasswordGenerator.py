# This program creates a random password using random.seed() to avoid reproducibility

import random
import string

voc = list(string.ascii_letters) + list(string.digits)

random.seed(123)

password = ''
size = 10

for i in range(size):
    random.shuffle(voc)

    password += voc[0]

print(f'Password Generated: \t{password}')