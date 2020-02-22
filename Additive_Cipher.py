#While incredibly short, this code strips off punctuation and spaces from the original message and treats everything as lowercase.
#It was written as quickly as possible for the purpose of submission as a lab assignment. 

from string import ascii_lowercase as lc #A string of all lowercase alphabets
from string import ascii_uppercase as uc #A string of all uppercase alphabets

def encode(s, k):
    l = [lc.index(i) for i in s.lower() if i.isalpha()] #Creates a list of indices of all letters in the input string
    return ''.join([uc[(i+k)%26] for i in l if not str(i).isspace()]) #Joins the string formed by shifting all the indices by key

def decode(s, k):
    l = [uc.index(i) for i in s.upper() if i.isalpha()] #Creates a list of indices of all letters in the input string
    return ''.join([lc[(i-k)%26] for i in l if not str(i).isspace()]) #Joins the string formed by shifting all the indices by key
