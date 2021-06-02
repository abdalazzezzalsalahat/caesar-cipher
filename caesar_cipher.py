from nltk.corpus import words
from collections import Counter
import nltk


words_list= words.words()
words = nltk.corpus.words.words()
print(len(words))


def encrypt(plain, key):
    """
    Function that takes in a plain text phrase and a numeric key and encrypts it using
    ceasar cipher with the shift equals to key. 
    """

    plain = plain.lower()
    encrypted_plain = ''
    key = key % 26

    for char in plain:

        if ord(char) not in range(97, 123):
            shifted_ascii = ord(char)
            encrypted_plain += chr(shifted_ascii)
            continue
        
        elif (ord(char)+key) > 122:
            steps_from_z = (122 - ord(char)) 
            steps_from_a = key  - steps_from_z - 1
            shifted_ascii = 97 + steps_from_a

        else:
            shifted_ascii = (ord(char)+ key) 
            
        encrypted_plain += chr(shifted_ascii)
  
    return encrypted_plain

def decrypt(enc_txt, key):
    """
    Function that takes in encrypted text and numeric key which will restore the encrypted 
    text back to its original form as long as correct key is supplied
    """

    return encrypt(enc_txt, -key)

def count_(sentences):
    w = sentences.split()
    c = 0
    for i in w:
        if i in words or i.upper() in words or i.lower() in words:
            c += 1
    return c



if __name__ == "__main__":
    assert encrypt('kill', 22) == 'gehh'
    assert encrypt('gym', 5) == 'ldr'
    assert encrypt('my name is azooz',27) == 'nz obnf jt bappa'
    assert decrypt('ectg',2) == 'care'

    print('All tests passed!!!!')

