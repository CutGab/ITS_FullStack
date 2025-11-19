# 6. Password Generator:

# Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
# Allow the user to specify the password length and desired character types.
# Generate and return a random password that meets the user's criteria.

import random
from string import *

def generate_password(length: int):

    possible_characters: list = []

    choice_1 = input("Would you like to use lowercase letters?: (Y/N)")

    if choice_1.lower() == "y":
        possible_characters.append(ascii_lowercase)

    choice_2 = input("Would you like to use uppercase letters?: (Y/N)")

    if choice_2.lower() == "y":
        possible_characters.append(ascii_uppercase)

    choice_3 = input("Would you like to use numbers?: (Y/N)")

    if choice_3.lower() == "y":
        possible_characters.append(digits)

    choice_4 = input("Would you like to use special characters?: (Y/N)")

    if choice_4.lower() == "y":
        possible_characters.append(punctuation)

    password = ""

    for _ in range(length):

        if possible_characters == []:
            print("Impossibile creare password, inserisca si almeno in un campo.")
            break

        else:
            stringa: str = random.choice(possible_characters)
            char: str = random.choice(stringa)
            password += char

    print(password)


generate_password(16)