import random

def dencrypt (message, key):

    ciphertext = ""

    for ch in message.upper():
        if str.isalpha(ch):
            new_letter_index = key[ord(ch) - ord('A')]
            new_letter = chr(new_letter_index + ord('A'))
            ciphertext += new_letter
        else:
            ciphertext += ch
    return ciphertext

encryption_key = list(range(26))
random.shuffle(encryption_key)

decryption_key = list(range(26))

#i will start at 0, and look at that position first

for i in range(26):
    decryption_key[encryption_key[i]] = i

plaintext = "Hello, World"

ciphertext = dencrypt(plaintext, encryption_key)
recovertext = dencrypt(ciphertext, decryption_key)

print(plaintext)
print(ciphertext)
print(recovertext)