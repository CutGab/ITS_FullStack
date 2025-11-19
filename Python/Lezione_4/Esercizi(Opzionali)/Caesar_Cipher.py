# 9. Caesar Cipher Encryption/Decryption

# Create functions for encrypting and decrypting a message using the Caesar cipher.
# Allow the user to specify the shift value (number of positions to shift each letter).
#  Handle both encryption and decryption using the same function with appropriate adjustments.
# Encrypt and decrypt the given message using the specified shift value.

from string import ascii_lowercase

def encrypt(text: str, key: int):

    encrypted_text: str = ""

    for char in text.lower():

        encrypted_text += ascii_lowercase[(ascii_lowercase.index(char) + key) % 26]

    print(encrypted_text)

def decrypt (text: str, key: int):

    decrypted_text: str = ""

    for char in text.lower():

        decrypted_text += ascii_lowercase[(ascii_lowercase.index(char) - key) % 26]

    print(decrypted_text)

encrypt("ciao", 5)
decrypt("hnft", 5)