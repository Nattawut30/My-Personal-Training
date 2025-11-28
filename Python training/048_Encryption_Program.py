# Python Encryption Program
# Fundamentals in CyberSecurity

import random
import string

# All the global Chars and special digits
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key  : {key}")

#ENCRYPT Text
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text: {plain_text}")
print(f"Encrypted text: {cipher_text}")

#DECRYPT Text
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted text: {cipher_text}")
print(f"Original text: {plain_text}")

