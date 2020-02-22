from string import ascii_lowercase as lc #A string of all lowercase alphabets
from string import ascii_uppercase as uc #A string of all uppercase alphabets

#Importing the module created in an earlier practical - link below
#https://raw.githubusercontent.com/ananda-sreenidhi/Cryptography-Practicals/master/Extended_Euclidean_Algorithm.py
from Extended_Euclidean_Algorithm import euclidean_gcd as modinv

def encrypt(s, k1, k2):
    l = [lc.index(i) for i in s.lower() if i.isalpha()] #List of indices of string contents, stripped of punctuation, spaces
    return ''.join([uc[(k1*x+k2)%26] for x in l if not str(x).isspace()]) #Joining list of alphabets shifted as per key
    
def decrypt(s, k1, k2):
    l = [uc.index(i) for i in s.upper() if i.isalpha()] #List of indices of string contents, stripped of punctuation, spaces
    return ''.join([lc[(modinv(k1, 26)*(x-k2))%26] for x in l if not str(x).isspace()]) #Joining list shifted as per key
