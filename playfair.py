"""
Playfair cipher
Implementation by github.com/justworm
Rewritten by github.com/ananda-sreenidhi
"""

from string import ascii_uppercase as alphabet #easy, don't need to make a list/string of alphabets
from collections import OrderedDict

def matrix(key):
    #OrderedDict helps add the letters from the key to the key matrix, and the next line adds the remaining letters except J. 
    matrix = [x for x in "".join(OrderedDict.fromkeys(key.upper()))] +\ 
             [x for x in alphabet if x not in key.upper() and x!="J"]
    #Reshapes the list into a 5x5 list
    return [matrix[x*5:(x*5)+5] for x in range(5)]

def digraphify(message_original):
    #A flag is chosen based on what letters the plaintext has (X if Z present, Z otherwise)
    flag = "Z" if 'x' in message_original.lower() else "X"
    #splits the message into individual letters
    l = list(''.join(message_original.upper().split(' ')))
    #flags double letters
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            l.insert(i+1, flag)
            continue
    #flags odd-length strings
    l.append(flag) if len(l)%2!=0 else True
    #creates digraphs
    message = [l[i]+l[i+1] for i in range(0, len(l), 2)]
    return message #returns list of digraphs

def find_matrix(matrix, letter):
    #function to find an element in a 2x2 list
    for i in matrix:
        if letter in i:
            return matrix.index(i), i.index(letter)

def encrypt(message, key):
    #encryption as per Playfair rules
    message = digraphify(message)
    key_matrix = matrix(key)
    cipher = []
    for x in message:
        a1, b1 = find_matrix(key_matrix, x[0])
        a2, b2 = find_matrix(key_matrix, x[1])
        if a1==a2:
            cipher.append(key_matrix[a1][(b1+1)%5])
            cipher.append(key_matrix[a1][(b2+1)%5])
        elif b1==b2:
            cipher.append(key_matrix[(a1+1)%5][b1])
            cipher.append(key_matrix[(a2+1)%5][b1])
        else:
            cipher.append(key_matrix[a1][b2])
            cipher.append(key_matrix[a2][b1])
    return ''.join(cipher)

def decrypt(cipher, key):
    #decryption as per Playfair rules
    cipher = digraphify(cipher)
    key_matrix = matrix(key)
    plaintext = []
    for x in cipher:
        a1, b1 = find_matrix(key_matrix, x[0])
        a2, b2 = find_matrix(key_matrix, x[1])
        if a1==a2:
            plaintext.append(key_matrix[a1][(b1-1)%5])
            plaintext.append(key_matrix[a1][(b2-1)%5])
        elif b1==b2:
            plaintext.append(key_matrix[(a1-1)%5][b1])
            plaintext.append(key_matrix[(a2-1)%5][b1])
        else:
            plaintext.append(key_matrix[a1][b2])
            plaintext.append(key_matrix[a2][b1])
    print(plaintext)
    if 'x' in ''.join(plaintext).lower() or 'z' in ''.join(plaintext).lower():
        for i in range(len(plaintext)-1):
            if plaintext[i]==plaintext[i+2] and plaintext[i+1].lower() in 'xz':
                flag = 'X' if plaintext[i+1] in 'xX' else 'Z'
                break
    return ''.join([x for x in plaintext if x.upper()!=flag]).lower().rstrip(flag.lower())
