# 10. Anagram Checker:

# Create a function that checks whether two given strings are anagrams of each other.
# Convert both strings to lowercase and remove any non-alphabetic characters.
# Sort the characters of each string and compare the sorted strings for equality.
# Indicate whether the strings are anagrams or not.

def anagram_checker(word: str, word_2: str):

    counter = 0

    for i in word:

        if i in word_2 and len(word) == len(word_2):
            counter += 1
    
    if counter == len(word):
        print("Sono anagrammi.")

    else:
        print("Non sono anagrammi.")


anagram_checker("pesca", "acsep")