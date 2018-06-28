#!/usr/bin/env python3

import hashlib


encrypt_types = ['SHA-1', 'MD5', 'SHA-256']

input_str = input('Enter string for encryption: ')
txt = 'Enter number of encription type\n'
i = 1
for x in encrypt_types:
    txt += '{!s}. {!s}\n'.format(i, x)
    i += 1
txt += 'Number: '
while True:
    try:
        encrypt_type_num = int(input(txt))
        encrypt_type = encrypt_types[encrypt_type_num - 1]
        break
    except Exception as e:
        print('Error: enter correct NUMBER')

hashed_str = ''

if encrypt_type == 'SHA-1':
    m = hashlib.sha1()
    m.update(bytes(input_str, encoding='utf-8'))
    hashed_str = m.hexdigest()
elif encrypt_type == 'MD5':
    m = hashlib.md5()
    m.update(bytes(input_str, encoding='utf-8'))
    hashed_str = m.hexdigest()
elif encrypt_type == 'SHA-256':
    m = hashlib.sha256()
    m.update(bytes(input_str, encoding='utf-8'))
    hashed_str = m.hexdigest()


print('Hashed string: {!s}'.format(hashed_str))
