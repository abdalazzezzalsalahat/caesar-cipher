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

def counter(sentences):
    """
    A function to count english words.
    """
    word = sentences.split()
    count = 0
    for i in word:
        if i in words or i.upper() in words or i.lower() in words:
            count += 1
    return count

def break_it(enc_txt):
    """Function to transform cipher into its original state without access to the key."""

    letters_count = Counter(enc_txt)

    del letters_count[',']
    del letters_count[' ']
    del letters_count['.']
    del letters_count[':']

    en_fingerprint = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p','g','w', 'y','b','v','k','x','j','q','z']

    possible_e = letters_count.most_common(1)[0][0]

    ''' check each letter from en_fingerprint until our text doesn't look like english text'''
    for letter in en_fingerprint:
        key = ord(possible_e) - ord(letter)
        decrypted_text = decrypt(enc_txt, key)
   
        if is_english(decrypted_text):
            return decrypted_text
  
    return "Not English"

def is_english(text):
  """Helper function to find out if the given text 
   is english text or not"""
  words = text.split()
  
  word_count = 0

  for word in words:
      
    if word in words_list:
      word_count += 1

  if (word_count/len(words)) > 0.5:
    return True

  else: 
    return False




if __name__ == "__main__":
    assert encrypt('kill', 22) == 'gehh'
    assert encrypt('gym', 5) == 'ldr'
    assert encrypt('my name is azooz',27) == 'nz obnf jt bappa'
    assert decrypt('ectg',2) == 'care'
    print(is_english('lskdfnnja'))
    print('\n\n\n\n')
    # print(counter('kjzsbhdduohy'))
    print('All tests passed!!!!')

